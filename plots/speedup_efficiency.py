import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

N_target = 100000
T_target = 10000

df_seq = pd.read_csv("../codes_and_jobs/seq_out_results.csv", skipinitialspace=True, names=["N", "T", "time"])
df_omp = pd.read_csv("../codes_and_jobs/omp_out_results.csv", skipinitialspace=True, names=["N", "T", "time", "threads"])
df_mpi = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", skipinitialspace=True, names=["N", "T", "time", "procs"])

seq_row = df_seq[(df_seq["N"] == N_target) & (df_seq["T"] == T_target)]
omp_rows = df_omp[(df_omp["N"] == N_target) & (df_omp["T"] == T_target)]
mpi_rows = df_mpi[(df_mpi["N"] == N_target) & (df_mpi["T"] == T_target)]

# Costruzione del DataFrame unificato
df_all = pd.DataFrame()

# Versione sequenziale
df_all = pd.concat([df_all, pd.DataFrame({
    "type": ["seq"],
    "p": [1],
    "time": seq_row["time"].values
})])

# OpenMP
df_all = pd.concat([df_all, pd.DataFrame({
    "type": "omp",
    "p": omp_rows["threads"],
    "time": omp_rows["time"]
})])

# MPI
df_all = pd.concat([df_all, pd.DataFrame({
    "type": "mpi",
    "p": mpi_rows["procs"],
    "time": mpi_rows["time"]
})])

# Calcolo speedup ed efficienza
T1 = df_all[df_all["type"] == "seq"]["time"].values[0]
df_all["speedup"] = T1 / df_all["time"]
df_all["efficiency"] = df_all["speedup"] / df_all["p"]

# Seleziona solo dati paralleli per i grafici
df_parallel = df_all[df_all["type"] != "seq"].sort_values(by=["type", "p"])
types = df_parallel["type"].unique()

# Plot con due grafici: efficienza e speedup
fig, axes = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Grafico dell'efficienza
for t in types:
    subset = df_parallel[df_parallel["type"] == t]
    axes[0].plot(subset["p"], subset["efficiency"], marker='o', label=t.upper())

axes[0].set_title(f"Efficiency (N={N_target}, T={T_target})")
axes[0].set_ylabel("Efficiency")
axes[0].grid(True)
axes[0].legend()

# Grafico dello speedup
for t in types:
    subset = df_parallel[df_parallel["type"] == t]
    axes[1].plot(subset["p"], subset["speedup"], marker='o', label=t.upper())

axes[1].set_title(f"Speedup (N={N_target}, T={T_target})")
axes[1].set_xlabel("Number of threads/processes")
axes[1].set_ylabel("Speedup")
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()


############################


N_target = 500000
T_target = 100000

df_seq = pd.read_csv("../codes_and_jobs/seq_out_results.csv", skipinitialspace=True, names=["N", "T", "time"])
df_omp = pd.read_csv("../codes_and_jobs/omp_out_results.csv", skipinitialspace=True, names=["N", "T", "time", "threads"])
df_mpi = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", skipinitialspace=True, names=["N", "T", "time", "procs"])

seq_row = df_seq[(df_seq["N"] == N_target) & (df_seq["T"] == T_target)]
omp_rows = df_omp[(df_omp["N"] == N_target) & (df_omp["T"] == T_target)]
mpi_rows = df_mpi[(df_mpi["N"] == N_target) & (df_mpi["T"] == T_target)]

# Costruzione del DataFrame unificato
df_all = pd.DataFrame()

# Versione sequenziale
df_all = pd.concat([df_all, pd.DataFrame({
    "type": ["seq"],
    "p": [1],
    "time": seq_row["time"].values
})])

# OpenMP
df_all = pd.concat([df_all, pd.DataFrame({
    "type": "omp",
    "p": omp_rows["threads"],
    "time": omp_rows["time"]
})])

# MPI
df_all = pd.concat([df_all, pd.DataFrame({
    "type": "mpi",
    "p": mpi_rows["procs"],
    "time": mpi_rows["time"]
})])

# Calcolo speedup ed efficienza
T1 = df_all[df_all["type"] == "seq"]["time"].values[0]
df_all["speedup"] = T1 / df_all["time"]
df_all["efficiency"] = df_all["speedup"] / df_all["p"]

# Seleziona solo dati paralleli per i grafici
df_parallel = df_all[df_all["type"] != "seq"].sort_values(by=["type", "p"])
types = df_parallel["type"].unique()

# Plot con due grafici: efficienza e speedup
fig, axes = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Grafico dell'efficienza
for t in types:
    subset = df_parallel[df_parallel["type"] == t]
    axes[0].plot(subset["p"], subset["efficiency"], marker='o', label=t.upper())

axes[0].set_title(f"Efficiency (N={N_target}, T={T_target})")
axes[0].set_ylabel("Efficiency")
axes[0].grid(True)
axes[0].legend()

# Grafico dello speedup
for t in types:
    subset = df_parallel[df_parallel["type"] == t]
    axes[1].plot(subset["p"], subset["speedup"], marker='o', label=t.upper())

axes[1].set_title(f"Speedup (N={N_target}, T={T_target})")
axes[1].set_xlabel("Number of threads/processes")
axes[1].set_ylabel("Speedup")
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()




#####################




N_target = 5000000
T_target = 100000

df_seq = pd.read_csv("../codes_and_jobs/seq_out_results.csv", skipinitialspace=True, names=["N", "T", "time"])
df_omp = pd.read_csv("../codes_and_jobs/omp_out_results.csv", skipinitialspace=True, names=["N", "T", "time", "threads"])
df_mpi = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", skipinitialspace=True, names=["N", "T", "time", "procs"])

seq_row = df_seq[(df_seq["N"] == N_target) & (df_seq["T"] == T_target)]
omp_rows = df_omp[(df_omp["N"] == N_target) & (df_omp["T"] == T_target)]
mpi_rows = df_mpi[(df_mpi["N"] == N_target) & (df_mpi["T"] == T_target)]

# Costruzione del DataFrame unificato
df_all = pd.DataFrame()

# Versione sequenziale
df_all = pd.concat([df_all, pd.DataFrame({
    "type": ["seq"],
    "p": [1],
    "time": seq_row["time"].values
})])

# OpenMP
df_all = pd.concat([df_all, pd.DataFrame({
    "type": "omp",
    "p": omp_rows["threads"],
    "time": omp_rows["time"]
})])

# MPI
df_all = pd.concat([df_all, pd.DataFrame({
    "type": "mpi",
    "p": mpi_rows["procs"],
    "time": mpi_rows["time"]
})])

# Calcolo speedup ed efficienza
T1 = df_all[df_all["type"] == "seq"]["time"].values[0]
df_all["speedup"] = T1 / df_all["time"]
df_all["efficiency"] = df_all["speedup"] / df_all["p"]

# Seleziona solo dati paralleli per i grafici
df_parallel = df_all[df_all["type"] != "seq"].sort_values(by=["type", "p"])
types = df_parallel["type"].unique()

# Plot con due grafici: efficienza e speedup
fig, axes = plt.subplots(2, 1, figsize=(10, 10), sharex=True)

# Grafico dell'efficienza
for t in types:
    subset = df_parallel[df_parallel["type"] == t]
    axes[0].plot(subset["p"], subset["efficiency"], marker='o', label=t.upper())

axes[0].set_title(f"Efficiency (N={N_target}, T={T_target})")
axes[0].set_ylabel("Efficiency")
axes[0].grid(True)
axes[0].legend()

# Grafico dello speedup
for t in types:
    subset = df_parallel[df_parallel["type"] == t]
    axes[1].plot(subset["p"], subset["speedup"], marker='o', label=t.upper())

axes[1].set_title(f"Speedup (N={N_target}, T={T_target})")
axes[1].set_xlabel("Number of threads/processes")
axes[1].set_ylabel("Speedup")
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()