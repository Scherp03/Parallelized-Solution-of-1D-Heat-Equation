import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("speedup_data.csv")  

T1 = df[df["type"] == "seq"]["time"].values[0]

df["speedup"] = T1 / df["time"]
df["efficiency"] = df["speedup"] / df["p"]

# Plot speedup
plt.figure(figsize=(8,5))
for label, group in df[df["type"] != "seq"].groupby("type"):
    plt.plot(group["p"], group["speedup"], marker='o', label=label.upper())

plt.title("Speedup")
plt.xlabel("Number of di threads/processes")
plt.ylabel("Speedup")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot efficiency
plt.figure(figsize=(8,5))
for label, group in df[df["type"] != "seq"].groupby("type"):
    plt.plot(group["p"], group["efficiency"], marker='o', label=label.upper())

plt.title("Efficiency")
plt.xlabel("Number of di threads/processes")
plt.ylabel("Efficiency")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
