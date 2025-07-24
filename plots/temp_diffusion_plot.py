import matplotlib.pyplot as plt
import numpy as np

# Lista dei file e relativi valori di T
files = [
    ("../codes_and_jobs/omp_results/temp_omp_N1000_T100000_threads2.csv", "T = 100.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N1000_T500000_threads2.csv", "T = 500.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N1000_T1000000_threads2.csv", "T = 1.000.000")
]

# Crea il grafico
for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("Final temperature diffusion with N = 1.000")
plt.grid(True)
plt.legend()
plt.show()

files = [
    ("../codes_and_jobs/omp_results/temp_omp_N5000_T100000_threads4.csv", "T = 100.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N5000_T500000_threads4.csv", "T = 500.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N5000_T1000000_threads4.csv", "T = 1.000.000")
]

# Crea il grafico
for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("Final temperature diffusion with N = 5.000")
plt.grid(True)
plt.legend()
plt.show()

files = [
    ("../codes_and_jobs/omp_results/temp_omp_N10000_T100000_threads4.csv", "T = 100.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N10000_T500000_threads4.csv", "T = 500.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N10000_T1000000_threads4.csv", "T = 1.000.000")
]

# Crea il grafico
for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("Final temperature diffusion with N = 10.000")
plt.grid(True)
plt.legend()
plt.show()