#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <omp.h>
#include <stdio.h>

// parameters
const int T = 50000;         // # of time steps
const int N = 10000;            // # of spatial points in the rod 
const double alpha = 0.01;    // thermic diffusivity
const double dx = 1.0 / N;       // spatial space (distance between two points along the rod, i.e. 0.01)
const double dt = 0.4 * dx * dx / alpha;        // temporal space (time of simulation step), 0.4 is used for stabilty according to the "G.D. Smith" book (chapter 5)

// coefficient for FTCS
const double r = alpha * dt / (dx * dx);

int main() {
    std::vector<double> u(N+1);
    std::vector<double> u_new(N+1);

    // distributed initialization as the example in "G.D. Smith" book (chapter 2)
    for (int i = 0; i <= N; ++i) {
        double x = i * dx;
        if (x <= 0.5)
            u[i] = 2 * x;
        else
            u[i] = 2 * (1 - x);
    }

    // write temperature distribution to a csv file (x, u[i]) = (position x, temperature at x)
    std::ofstream out_t("init_temp_seq.csv"); 
    for (int i = 0; i < N; ++i) {
        double x = i * dx;
        out_t << x << "," << u[i] << "\n";
    }
    out_t.close();

    double start_time = omp_get_wtime();

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

        // copy of u_new in u for the next step
        for (int i = 0; i < N; ++i) {
            u[i] = u_new[i];
        }
    }

    double end_time = omp_get_wtime();
    std::cout << "Threads: " << omp_get_max_threads() << "\n";
    std::cout << "Execution time: " << (end_time - start_time) << " seconds\n";

    // write output to a csv file (x, u[i]) = (position x, temperature at x)
    std::ofstream out("final_temp_seq.csv"); 
    for (int i = 0; i < N; ++i) {
        double x = i * dx;
        out << x << "," << u[i] << "\n";
    }
    out.close();

    std::cout << "\nFinished \n";
    return 0;
}

// export OMP_NUM_THREADS=1
// ./omp
// export OMP_NUM_THREADS=2
// ./omp
// export OMP_NUM_THREADS=4
// ./omp