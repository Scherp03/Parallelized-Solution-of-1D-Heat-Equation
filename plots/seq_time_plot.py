import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../codes_and_jobs/seq_out_results.csv", header=None, names=["N", "T", "time", "threads"])

df["label"] = df.apply(lambda row: f"N={row['N']}, T={row['T']}", axis=1)

plt.figure(figsize=(12, 6))
plt.bar(df["label"], df["time"], color="purple")
plt.title("Execution time per each pair (N, T)")
plt.xlabel("Combination of N and T ")
plt.ylabel("Execution time (s)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()