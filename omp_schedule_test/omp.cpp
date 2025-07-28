#include <iostream>
#include <vector>
#include <cmath>
#include <omp.h>
#include <string>

int main(int argc, char* argv[]) {
    if (argc < 5) {
        std::cerr << "Uso: " << argv[0] << " N T schedule chunk\n";
        return 1;
    }

    int N = std::stoi(argv[1]);
    int T = std::stoi(argv[2]);
    std::string sched_type = argv[3];
    int chunk = std::stoi(argv[4]);

    if (sched_type == "static")
        omp_set_schedule(omp_sched_static, chunk);
    else if (sched_type == "dynamic")
        omp_set_schedule(omp_sched_dynamic, chunk);
    else if (sched_type == "guided")
        omp_set_schedule(omp_sched_guided, chunk);
    else {
        std::cerr << "Errore: tipo di schedule non valido\n";
        return 1;
    }

    std::vector<double> u(N, 0.0);
    std::vector<double> u_new(N, 0.0);

    const double dx = 1.0 / (N - 1);
    const double dt = 0.4 * dx * dx;
    const double r = dt / (dx * dx);

    u[N / 4] = 100.0;
    u[N / 2] = 60.0;

    double start = omp_get_wtime();

    #pragma omp parallel
    {
        for (int t = 0; t < T; ++t) {
            #pragma omp for schedule(runtime)
            for (int i = 1; i < N - 1; ++i) {
                u_new[i] = u[i] + r * (u[i + 1] - 2 * u[i] + u[i - 1]);
            }

            #pragma omp single
            {
                std::swap(u, u_new);
            }
        }
    }

    double end = omp_get_wtime();

    omp_sched_t actual_sched;
    int actual_chunk;
    omp_get_schedule(&actual_sched, &actual_chunk);

    std::string sched_name = (actual_sched == omp_sched_static) ? "static" :
                             (actual_sched == omp_sched_dynamic) ? "dynamic" :
                             (actual_sched == omp_sched_guided) ? "guided" : "unknown";

    std::cout << sched_name << "," << actual_chunk << "," << omp_get_max_threads() << "," << (end - start) << std::endl;

    return 0;
}
