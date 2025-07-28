import pandas as pd
import matplotlib.pyplot as plt

# Caricamento dati
seq_df = pd.read_csv("../codes_and_jobs/seq_out_results.csv", header=None, names=["N", "T", "Time"])
omp_df = pd.read_csv("../codes_and_jobs/omp_out_results.csv", header=None, names=["N", "T", "Time", "Threads"])
mpi_df = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", header=None, names=["N", "T", "Time", "Processes"])

# Configurazioni da includere
parallel_levels = [2, 4, 8, 16, 32]

# Raggruppamento
seq_grouped = seq_df.groupby(["N", "T"]).mean().reset_index()
omp_grouped = omp_df[omp_df["Threads"].isin(parallel_levels)].groupby(["N", "T", "Threads"]).mean().reset_index()
mpi_grouped = mpi_df[mpi_df["Processes"].isin(parallel_levels)].groupby(["N", "T", "Processes"]).mean().reset_index()

# Lista dei valori unici di N
unique_N = sorted(seq_grouped["N"].unique())
bar_width = 0.06

# === PLOT PER OGNI N ===
for n_val in unique_N:
    seq_n = seq_grouped[seq_grouped["N"] == n_val]
    omp_n = omp_grouped[omp_grouped["N"] == n_val]
    mpi_n = mpi_grouped[mpi_grouped["N"] == n_val]

    labels = seq_n["T"].astype(str).tolist()
    x = list(range(len(labels)))

    plt.figure(figsize=(18, 6))

    offset = -5 * bar_width  # 11 barre in totale: da -5 a +5

    # 1. Sequential
    plt.bar([i + offset for i in x], seq_n["Time"], width=bar_width, label="Sequential")
    offset += bar_width

    # 2. OMP (2, 4, 8, 16, 32)
    for threads in parallel_levels:
        omp_t = omp_n[omp_n["Threads"] == threads].set_index("T").reindex(seq_n["T"]).reset_index()
        plt.bar([i + offset for i in x], omp_t["Time"], width=bar_width, label=f"OMP ({threads} threads)")
        offset += bar_width

    # 3. MPI (2, 4, 8, 16, 32)
    for procs in parallel_levels:
        mpi_t = mpi_n[mpi_n["Processes"] == procs].set_index("T").reindex(seq_n["T"]).reset_index()
        plt.bar([i + offset for i in x], mpi_t["Time"], width=bar_width, label=f"MPI ({procs} processes)")
        offset += bar_width

    plt.xticks(x, labels, rotation=45)
    plt.xlabel(f"T")
    plt.ylabel("Execution time (s)")
    plt.title(f"Execution Time Comparison for T (N = {n_val})")
    plt.legend(ncol=2)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()
