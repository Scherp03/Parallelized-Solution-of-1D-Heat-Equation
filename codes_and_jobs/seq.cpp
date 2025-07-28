#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <chrono>

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

    std::vector<double> u(N+1);
    std::vector<double> u_new(N+1);

    // simple initialization
    for (int i = 0; i < N; ++i) {
        u[i] = 0.0;
    }
    u[N / 4] = 100.0; 
    u[N/2] = 60.0;

    // triangle initialization as the example in "G.D. Smith" book (chapter 2)
    // for (int i = 0; i <= N; ++i) {
    //     // scaled
    //     double x = i * dx;
    //     if (x <= 0.5)
    //         u[i] = 2 * x;
    //     else
    //         u[i] = 2 * (1 - x);
    // }

    auto start = std::chrono::high_resolution_clock::now();

    // temporal diffusion
    for (int t = 0; t < T; ++t) {
        // fixed boundaries conditions
        u_new[0] = 0.0;
        u_new[N - 1] = 0.0;

        // FTCS (forward time, central space) on internal points
        for (int i = 1; i < N - 1; ++i) {
            u_new[i] = u[i] + r * (u[i+1] - 2*u[i] + u[i-1]);
        }

        // copy of u_new in u for the next step
        // for (int i = 0; i < N; ++i) {
        //     u[i] = u_new[i];
        // }

        // directly swap pointers, more efficient then copying in for loop
        std::swap(u, u_new);
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    double exec_time = duration.count();

    // write output to a csv file (x, u[i]) = (position x, temperature at x)
    std::string filename = "seq_results/temp_seq_N" + std::to_string(N) + "_T" + std::to_string(T) + ".csv";
    std::ofstream res(filename); 
    for (int i = 0; i < N; ++i) {
        double x = i * dx;
        res << x << "," << u[i] << "\n";
    }
    res.close();

    // write data to csv file
    std::ofstream out("seq_out_results.csv", std::ios::app); 
    out << N << "," << T << "," << exec_time << "\n";
    out.close();
    
    return 0;
}

