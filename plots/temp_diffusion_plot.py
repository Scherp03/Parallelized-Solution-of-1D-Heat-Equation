import matplotlib.pyplot as plt
import numpy as np

# Lista dei file e relativi valori di T
files = [
    ("../codes_and_jobs/seq_results/temp_seq_N1000_T100000.csv", "T = 100.000"),
    ("../codes_and_jobs/seq_results/temp_seq_N1000_T500000.csv", "T = 500.000"),
    ("../codes_and_jobs/seq_results/temp_seq_N1000_T1000000.csv", "T = 1.000.000")
]

# Crea il grafico
for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("SEQ Final temperature diffusion with N = 1.000")
plt.grid(True)
plt.legend()
plt.show()


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
plt.title("OMP Final temperature diffusion with N = 1.000")
plt.grid(True)
plt.legend()
plt.show()


# Lista dei file e relativi valori di T
files = [
    ("../codes_and_jobs/mpi_results/temp_mpi_N1000_T100000_procs2.csv", "T = 100.000"),
    ("../codes_and_jobs/mpi_results/temp_mpi_N1000_T500000_procs2.csv", "T = 500.000"),
    ("../codes_and_jobs/mpi_results/temp_mpi_N1000_T1000000_procs2.csv", "T = 1.000.000")
]

# Crea il grafico
for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("MPIFinal temperature diffusion with N = 1.000")
plt.grid(True)
plt.legend()
plt.show()









# Lista dei file e relativi valori di T
files = [
    ("../codes_and_jobs/seq_results/temp_seq_N5000_T100000.csv", "T = 100.000"),
    ("../codes_and_jobs/seq_results/temp_seq_N5000_T500000.csv", "T = 500.000"),
    ("../codes_and_jobs/seq_results/temp_seq_N5000_T1000000.csv", "T = 1.000.000")
]

# Crea il grafico
for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("SEQ Final temperature diffusion with N = 5.000")
plt.grid(True)
plt.legend()
plt.show()


# Lista dei file e relativi valori di T
files = [
    ("../codes_and_jobs/omp_results/temp_omp_N5000_T100000_threads2.csv", "T = 100.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N5000_T500000_threads2.csv", "T = 500.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N5000_T1000000_threads2.csv", "T = 1.000.000")
]

# Crea il grafico
for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("OMP Final temperature diffusion with N = 5.000")
plt.grid(True)
plt.legend()
plt.show()


# Lista dei file e relativi valori di T
files = [
    ("../codes_and_jobs/mpi_results/temp_mpi_N5000_T100000_procs2.csv", "T = 100.000"),
    ("../codes_and_jobs/mpi_results/temp_mpi_N5000_T500000_procs2.csv", "T = 500.000"),
    ("../codes_and_jobs/mpi_results/temp_mpi_N5000_T1000000_procs2.csv", "T = 1.000.000")
]

# Crea il grafico
for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("MPI Final temperature diffusion with N = 5.000")
plt.grid(True)
plt.legend()
plt.show()





# Lista dei file e relativi valori di T
files = [
    ("../codes_and_jobs/seq_results/temp_seq_N10000_T100000.csv", "T = 100.000"),
    ("../codes_and_jobs/seq_results/temp_seq_N10000_T500000.csv", "T = 500.000"),
    ("../codes_and_jobs/seq_results/temp_seq_N10000_T1000000.csv", "T = 1.000.000")
]

# Crea il grafico
for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("SEQ Final temperature diffusion with N = 10.000")
plt.grid(True)
plt.legend()
plt.show()


# Lista dei file e relativi valori di T
files = [
    ("../codes_and_jobs/omp_results/temp_omp_N10000_T100000_threads2.csv", "T = 100.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N10000_T500000_threads2.csv", "T = 500.000"),
    ("../codes_and_jobs/omp_results/temp_omp_N10000_T1000000_threads2.csv", "T = 1.000.000")
]

# Crea il grafico
for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("OMP Final temperature diffusion with N = 10.000")
plt.grid(True)
plt.legend()
plt.show()


# Lista dei file e relativi valori di T
files = [
    ("../codes_and_jobs/mpi_results/temp_mpi_N10000_T100000_procs2.csv", "T = 100.000"),
    ("../codes_and_jobs/mpi_results/temp_mpi_N10000_T500000_procs2.csv", "T = 500.000"),
    ("../codes_and_jobs/mpi_results/temp_mpi_N10000_T1000000_procs2.csv", "T = 1.000.000")
]

# Crea il grafico
for filename, label in files:
    data = np.loadtxt(filename, delimiter=",")
    x = data[:, 0]
    u = data[:, 1]
    plt.plot(x, u, label=label)

  
plt.xlabel("x (along rod)")
plt.ylabel("temperature u(x)")
plt.title("MPI Final temperature diffusion with N = 10.000")
plt.grid(True)
plt.legend()
plt.show()
