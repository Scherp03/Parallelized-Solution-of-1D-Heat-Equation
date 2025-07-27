import pandas as pd
import matplotlib.pyplot as plt

# Caricamento dei file CSV
seq_df = pd.read_csv("../codes_and_jobs/seq_out_results.csv", header=None, names=["N", "T", "Time"])
omp_df = pd.read_csv("../codes_and_jobs/omp_out_results.csv", header=None, names=["N", "T", "Time", "Threads"])
mpi_df = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", header=None, names=["N", "T", "Time", "Processes"])

# Filtro: solo 4, 8, 32 thread/processi per OMP e MPI
omp_filtered = omp_df[omp_df["Threads"].isin([4, 8, 32])]
mpi_filtered = mpi_df[mpi_df["Processes"].isin([4, 8, 32])]

# Raggruppamento per N e T (media dei tempi se ci sono più misurazioni)
seq_grouped = seq_df.groupby(["N", "T"]).mean().reset_index()
omp_grouped = omp_filtered.groupby(["N", "T", "Threads"]).mean().reset_index()
mpi_grouped = mpi_filtered.groupby(["N", "T", "Processes"]).mean().reset_index()

# Funzione per creare etichette univoche sull'asse X
def make_labels(df):
    return df[["N", "T"]].astype(str).agg("x".join, axis=1)

# Preparazione del grafico
plt.figure(figsize=(12, 6))

# Plot sequenziale
plt.plot(make_labels(seq_grouped), seq_grouped["Time"], label="Sequential", marker="o")

# Plot OMP
for threads in [4, 8, 32]:
    subset = omp_grouped[omp_grouped["Threads"] == threads]
    label = f"OMP ({threads} threads)"
    plt.plot(make_labels(subset), subset["Time"], label=label, marker="o")

# Plot MPI
for procs in [4, 8, 32]:
    subset = mpi_grouped[mpi_grouped["Processes"] == procs]
    label = f"MPI ({procs} processi)"
    plt.plot(make_labels(subset), subset["Time"], label=label, marker="o")

# Etichette e stile del grafico
plt.xlabel("N x T")
plt.ylabel("Tempo (s)")
plt.title("Confronto tempi di esecuzione: Sequenziale, OMP e MPI")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
