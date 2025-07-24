import pandas as pd
import matplotlib.pyplot as plt

# Leggi il CSV (sostituisci 'dati.csv' con il nome del tuo file)
df = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", header=None, names=["N", "T", "time", "procs"])

# Ordina per chiarezza
df.sort_values(by=["N", "T", "procs"], inplace=True)

# Raggruppa per combinazioni di N e T
grouped = df.groupby(["N", "T"])

# Crea un unico grafico
plt.figure(figsize=(10, 6))

# Colori e label per ogni curva
for (n, t), group in grouped:
    label = f"N={n}, T={t}"
    plt.plot(group["procs"], group["time"], marker="o", label=label)

plt.title("MPI Time VS Threads")
plt.xlabel("Number of threads")
plt.ylabel("Execution time (s)")
plt.grid(True)
plt.legend()
plt.xticks(sorted(df["procs"].unique()))
plt.tight_layout()
plt.show()