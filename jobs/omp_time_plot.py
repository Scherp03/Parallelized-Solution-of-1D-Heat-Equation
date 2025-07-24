import pandas as pd
import matplotlib.pyplot as plt

# Leggi il CSV (sostituisci 'dati.csv' con il nome del tuo file)
df = pd.read_csv("omp_out_results.csv", header=None, names=["N", "T", "time", "threads"])

# Ordina per chiarezza
df.sort_values(by=["N", "T", "threads"], inplace=True)

# Raggruppa per combinazioni di N e T
grouped = df.groupby(["N", "T"])

# Crea un unico grafico
plt.figure(figsize=(10, 6))

# Colori e label per ogni curva
for (n, t), group in grouped:
    label = f"N={n}, T={t}"
    plt.plot(group["threads"], group["time"], marker="o", label=label)

plt.title("OpenMP Time VS Threads")
plt.xlabel("Number of threads")
plt.ylabel("Execution time (s)")
plt.grid(True)
plt.legend()
plt.xticks(sorted(df["threads"].unique()))
plt.tight_layout()
plt.show()