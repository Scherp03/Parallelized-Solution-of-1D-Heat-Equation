#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <omp.h>
#include <stdio.h>

int main(int argc, char** argv) {

        if (argc != 3) {
        std::cerr << "Error! Missing Parameters : " << argv[0] << " N T\n";
        std::cerr << "Example: " << argv[0] << " 100000 5000\n";
        return 1;
    }
    // parameters
    const int N = std::stoi(argv[1]);         // # of spatial points in the rod 
    const int T = std::stoi(argv[2]);         // # of time steps
    const double alpha = 0.01;    // thermic diffusivity
    const double dx = 1.0 / N;       // spatial space (distance between two points along the rod, i.e. 0.01)
    const double dt = 0.4 * dx * dx / alpha;        // temporal space (time of simulation step), 0.4 is used for stabilty according to the "G.D. Smith" book (chapter 5)

    // coefficient for FTCS
    const double r = alpha * dt / (dx * dx);

    double start_time, end_time;

    std::vector<double> u(N+1);
    std::vector<double> u_new(N+1);

    // simple initialization
    for (int i = 0; i < N; ++i) {
        u[i] = 0.0;
    }
    u[N / 4] = 100.0; 
    u[N/2] = 60.0;

    // distributed initialization as the example in "G.D. Smith" book (chapter 2)
    //for (int i = 0; i <= N; ++i) {
    //    double x = i * dx;
    //    if (x <= 0.5)
    //        u[i] = 2 * x;
    //    else
    //        u[i] = 2 * (1 - x);
    //}

    // write temperature distribution to a csv file (x, u[i]) = (position x, temperature at x)
    // std::ofstream out_t("init_temp_omp.csv"); 
    // for (int i = 0; i < N; ++i) {
    //     double x = i * dx;
    //     out_t << x << "," << u[i] << "\n";
    // }
    // out_t.close();

    start_time = omp_get_wtime();

    // temporal diffusion
    for (int t = 0; t < T; ++t) {
        // fixed boundaries conditions
        u_new[0] = 0.0;
        u_new[N - 1] = 0.0;

        // FTCS (forward time, central space) on internal points
        // no need for private(...) or shared(...)
        // i is the loop variable (automatically private)
        // u and u_new are accessed safely by threads at different positions
        #pragma omp parallel for schedule(static)
        for (int i = 1; i < N - 1; ++i) {
            u_new[i] = u[i] + r * (u[i+1] - 2*u[i] + u[i-1]);
        }

        // directly swap pointers, more efficient then copying in for loop
        std::swap(u, u_new);
    }

    end_time = omp_get_wtime();
    int threads = omp_get_num_threads();
    double exec_time = (end_time - start_time);
    std::cout << "Threads: " << threads << std::endl;
    std::cout << "Execution time: " << exec_time << " seconds" << std::endl;

    // write output to a csv file (x, u[i]) = (position x, temperature at x)
    std::string filename = "omp_results/temp_omp_N" + std::to_string(N) + "_T" + std::to_string(T) + "_threads" + std::to_string(threads) + ".csv";
    std::ofstream res(filename); 
    for (int i = 0; i < N; ++i) {
        double x = i * dx;
        res << x << "," << u[i] << "\n";
    }
    res.close();

    // write data to csv file
    std::ofstream out("omp_out_results.csv", std::ios::app); 
    out << N << "," << T << "," << exec_time << "," << threads << "\n";
    out.close();

    std::cout << "\nN = " << N << std::endl;
    std::cout << "T = " << T << std::endl;
    return 0;
}

// export OMP_NUM_THREADS=1
// ./omp
// export OMP_NUM_THREADS=2
// ./omp
// export OMP_NUM_THREADS=4
// ./omp
