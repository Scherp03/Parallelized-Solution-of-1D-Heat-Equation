#include <iostream>
#include <fstream>
#include <vector>
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {

    if (argc != 3) {
        std::cerr << "Error! Missing Parameters : " << argv[0] << " N T\n";
        std::cerr << "Example: " << argv[0] << " 100000 5000\n";
        exit(0);
    }
    // parameters
    const int N = std::stoi(argv[1]);         // # of spatial points in the rod 
    const int T = std::stoi(argv[2]);         // # of time steps
    const double alpha = 0.01;    // thermic diffusivity
    const double dx = 1.0 / N;       // spatial space (distance between two points along the rod, i.e. 0.01)
    const double dt = 0.4 * dx * dx / alpha;        // temporal space (time of simulation step), 0.4 is used for stabilty according to the "G.D. Smith" book (chapter 2)

    // coefficient for FTCS
    const double r = alpha * dt / (dx * dx);

    MPI_Init(&argc, &argv);

    // size => total # of processes; rank => current process
    int size, rank;

    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
 
    // divide domain into processes
    int local_N = N / size;
    // if something's left, it's assigned to the last process
    if (rank == size - 1) { 
        local_N += N % size; 
    }

    double start_time, end_time;

    // 2 extra cells to communicate with neighbors
    std::vector<double> u(local_N + 2);     
    std::vector<double> u_new(local_N + 2);


    int start = rank * (N / size);            
    int end = (rank + 1) * (N / size); 

    // simple initialization
    for (int i = 0; i <= local_N; ++i) {
        u[i] = 0.0;
    }
    if (N / 4 >= start && N / 4 < end) {
        int local_index = (N / 4) - start;
        u[local_index + 1] = 100.0;
    }
    if (N / 2 >= start && N / 2 < end) {
        int local_index = (N / 2) - start;
        u[local_index + 1] = 60.0;
    }

    start_time = MPI_Wtime();

    for (int t = 0; t < T; t++) {
        bool left_neighbor = rank > 0;
        bool right_neighbor = rank < size - 1;
        MPI_Request req_send_left, req_send_right, req_recv_left, req_recv_right;

        // asynchronous communication
        if (left_neighbor) {
            MPI_Isend(&u[1], 1, MPI_DOUBLE, rank - 1, 0, MPI_COMM_WORLD, &req_send_left);
            MPI_Irecv(&u[0], 1, MPI_DOUBLE, rank - 1, 1, MPI_COMM_WORLD, &req_recv_left);
        }

        if (right_neighbor) {
            MPI_Isend(&u[local_N], 1, MPI_DOUBLE, rank + 1, 1, MPI_COMM_WORLD, &req_send_right);
            MPI_Irecv(&u[local_N + 1], 1, MPI_DOUBLE, rank + 1, 0, MPI_COMM_WORLD, &req_recv_right);
        }

        // FTCS (forward time, central space) on internal points
        // from 2 to local_N - 1, 1 and local_N are the border points, 0 and local_N+1 are the external points
        for (int i = 2; i < local_N; ++i) {
            u_new[i] = u[i] + r * (u[i+1] - 2*u[i] + u[i-1]);
        }

        // wait for communication to complete
        if (left_neighbor) {
            MPI_Wait(&req_send_left, MPI_STATUS_IGNORE);
            MPI_Wait(&req_recv_left, MPI_STATUS_IGNORE);
        }

        if (right_neighbor) {
            MPI_Wait(&req_send_right, MPI_STATUS_IGNORE);
            MPI_Wait(&req_recv_right, MPI_STATUS_IGNORE);
        }

        // compute boundary points
        if (local_N >= 1) {
            u_new[1] = u[1] + r * (u[2] - 2 * u[1] + u[0]);
            u_new[local_N] = u[local_N] + r * (u[local_N + 1] - 2 * u[local_N] + u[local_N - 1]);
        }

        // fixed boundaries conditions
        if (rank == 0) {
            u_new[1] = 0.0;  
        }
        if (rank == size - 1) {
            u_new[local_N] = 0.0; 
        }

        // directly swap pointers, more efficient then copying in for loop
        std::swap(u, u_new);
    }

    end_time = MPI_Wtime();
    double local_time = end_time - start_time;

    // parameter and function to measure worst case time (end of code)
    double max_time;
    MPI_Reduce(&local_time, &max_time, 1, MPI_DOUBLE, MPI_MAX, 0, MPI_COMM_WORLD);

    // write to csv file at last process 0
    if (rank == 0) {
        std::string filename = "mpi_async_results/temp_mpi_async_N" + std::to_string(N) + "_T" + std::to_string(T) + "_procs" + std::to_string(size) + ".csv";
        std::ofstream res(filename); 
        // write data of process 0
        for (int i = 1; i <= local_N; ++i) {
            double x = dx * (i - 1);
            res << x << "," << u[i] << "\n";
        }
        // write data of other processes
        for (int p = 1; p < size; ++p) {
            int recv_N = N / size;
            if (p == size - 1) { 
                recv_N += N % size;
            }
            std::vector<double> buffer(recv_N);
            MPI_Recv(buffer.data(), recv_N, MPI_DOUBLE, p, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            // if (p == size -1 ) {
                for (int i = 0; i < recv_N; ++i) {
                    double x = dx * (p * (N / size) + i);
                    res << x << "," << buffer[i] << "\n";
                }
            // } else {
            //     for (int i = 0; i <= recv_N; ++i) {
            //         double x = dx * (p * (N / size) + i);
            //         res << x << "," << buffer[i] << "\n";
            //     }
            // }
        }
        res.close();
    } else {
        // send computed data to rank 0
        MPI_Send(&u[1], local_N, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD);
    }
    MPI_Finalize();

    // print worst case time
    if (rank == 0) {

        // write data to csv file
        std::ofstream out("mpi_async_out_results.csv", std::ios::app); 
        out << N << "," << T << "," << max_time << "," << size << "\n";
        out.close();
    }
    return 0;
}
