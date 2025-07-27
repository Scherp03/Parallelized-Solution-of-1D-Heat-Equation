import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("speedup_eff_N10000_T1000000.csv")

# Calcolo speedup ed efficiency
T1 = df[df["type"] == "seq"]["time"].values[0]
df["speedup"] = T1 / df["time"]
df["efficiency"] = df["speedup"] / df["p"]

# Filtra dati escludendo la versione sequenziale
df_parallel = df[df["type"] != "seq"]

# Ordina i dati per tipo e numero di processori
df_parallel = df_parallel.sort_values(by=["type", "p"])

# Ottieni lista dei tipi e dei valori unici di p
types = df_parallel["type"].unique()
p_values = sorted(df_parallel["p"].unique())

# Larghezza delle barre e posizione
bar_width = 0.8 / len(types)
x = np.arange(len(p_values))

# Istogramma Speedup
plt.figure(figsize=(9, 5))
for i, t in enumerate(types):
    data = df_parallel[df_parallel["type"] == t]
    plt.bar(x + i * bar_width, data["speedup"], width=bar_width, label=t.upper())

plt.title("Speedup")
plt.xlabel("Number of threads/processes")
plt.ylabel("Speedup")
plt.xticks(x + bar_width * (len(types)-1)/2, p_values)
plt.grid(axis="y")
plt.legend()
plt.tight_layout()
plt.show()

# Istogramma Efficiency
plt.figure(figsize=(9, 5))
for i, t in enumerate(types):
    data = df_parallel[df_parallel["type"] == t]
    plt.bar(x + i * bar_width, data["efficiency"], width=bar_width, label=t.upper())

plt.title("Efficiency")
plt.xlabel("Number of threads/processes")
plt.ylabel("Efficiency")
plt.xticks(x + bar_width * (len(types)-1)/2, p_values)
plt.grid(axis="y")
plt.legend()
plt.tight_layout()
plt.show()
