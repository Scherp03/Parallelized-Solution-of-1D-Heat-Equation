import matplotlib.pyplot as plt
import numpy as np


files = [
    ("../codes_and_jobs/seq_results/temp_seq_N100000_T10000.csv", "T = 10.000"),
    ("../codes_and_jobs/seq_results/temp_seq_N100000_T100000.csv", "T = 100.000")
]


for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("SEQ Final temperature diffusion with N = 100.000")
plt.grid(True)
plt.legend()
plt.show()


files = [
    ("../codes_and_jobs/omp_results/temp_omp_N100000_T10000_threads2.csv", "T = 10.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N100000_T100000_threads2.csv", "T = 100.000")
]

for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("OMP Final temperature diffusion with N = 100.000")
plt.grid(True)
plt.legend()
plt.show()


files = [
    ("../codes_and_jobs/mpi_results/temp_mpi_N100000_T10000_procs2.csv", "T = 10.000"),
    ("../codes_and_jobs/mpi_results/temp_mpi_N100000_T100000_procs2.csv", "T = 100.000")
]

for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("MPIFinal temperature diffusion with N = 100.000")
plt.grid(True)
plt.legend()
plt.show()




files = [
    ("../codes_and_jobs/seq_results/temp_seq_N500000_T10000.csv", "T = 10.000"),
    ("../codes_and_jobs/seq_results/temp_seq_N500000_T100000.csv", "T = 100.000")
]


for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("SEQ Final temperature diffusion with N = 500.000")
plt.grid(True)
plt.legend()
plt.show()


files = [
    ("../codes_and_jobs/omp_results/temp_omp_N500000_T10000_threads2.csv", "T = 10.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N500000_T100000_threads2.csv", "T = 100.000")
]

for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("OMP Final temperature diffusion with N = 500.000")
plt.grid(True)
plt.legend()
plt.show()


files = [
    ("../codes_and_jobs/mpi_results/temp_mpi_N500000_T10000_procs2.csv", "T = 10.000"),
    ("../codes_and_jobs/mpi_results/temp_mpi_N500000_T100000_procs2.csv", "T = 100.000")
]

for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("MPIFinal temperature diffusion with N = 500.000")
plt.grid(True)
plt.legend()
plt.show()





files = [
    ("../codes_and_jobs/seq_results/temp_seq_N1000000_T10000.csv", "T = 10.000"),
    ("../codes_and_jobs/seq_results/temp_seq_N1000000_T100000.csv", "T = 100.000")
]


for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("SEQ Final temperature diffusion with N = 1.000.000")
plt.grid(True)
plt.legend()
plt.show()


files = [
    ("../codes_and_jobs/omp_results/temp_omp_N1000000_T10000_threads2.csv", "T = 10.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N1000000_T100000_threads2.csv", "T = 100.000")
]

for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("OMP Final temperature diffusion with N = 1.000.000")
plt.grid(True)
plt.legend()
plt.show()


files = [
    ("../codes_and_jobs/mpi_results/temp_mpi_N1000000_T10000_procs2.csv", "T = 10.000"),
    ("../codes_and_jobs/mpi_results/temp_mpi_N1000000_T100000_procs2.csv", "T = 100.000")
]

for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("MPIFinal temperature diffusion with N = 1.000.000")
plt.grid(True)
plt.legend()
plt.show()




files = [
    ("../codes_and_jobs/seq_results/temp_seq_N5000000_T10000.csv", "T = 10.000"),
    ("../codes_and_jobs/seq_results/temp_seq_N5000000_T100000.csv", "T = 100.000")
]


for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("SEQ Final temperature diffusion with N = 5.000.000")
plt.grid(True)
plt.legend()
plt.show()


files = [
    ("../codes_and_jobs/omp_results/temp_omp_N5000000_T10000_threads2.csv", "T = 10.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N5000000_T100000_threads2.csv", "T = 100.000")
]

for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("OMP Final temperature diffusion with N = 5.000.000")
plt.grid(True)
plt.legend()
plt.show()


files = [
    ("../codes_and_jobs/mpi_results/temp_mpi_N5000000_T10000_procs2.csv", "T = 10.000"),
    ("../codes_and_jobs/mpi_results/temp_mpi_N5000000_T100000_procs2.csv", "T = 100.000")
]

for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("MPIFinal temperature diffusion with N = 5.000.000")
plt.grid(True)
plt.legend()
plt.show()
