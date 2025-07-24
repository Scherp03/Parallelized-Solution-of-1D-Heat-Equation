import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../codes_and_jobs/omp_out_results.csv", header=None, names=["N", "T", "time", "threads"])

df_filtered = df[(df["N"] == 1000) & (df["T"] == 100000)].copy()

df_filtered.sort_values(by="threads", inplace=True)

plt.figure(figsize=(10, 6))

plt.plot(df_filtered["threads"], df_filtered["time"], marker="o", label="N=1000, T=100000")

plt.title("OpenMP: Execution Time VS Threads (N=1.000, T=100.000)")
plt.xlabel("Number of threads")
plt.ylabel("Execution time (s)")
plt.grid(True)
plt.legend()
plt.xticks(sorted(df["threads"].unique()))
plt.tight_layout()
plt.show()


# N and T different 

df = pd.read_csv("../codes_and_jobs/omp_out_results.csv", header=None, names=["N", "T", "time", "threads"])

df_filtered = df[(df["N"] == 10000) & (df["T"] == 1000000)].copy()

df_filtered.sort_values(by="threads", inplace=True)

plt.figure(figsize=(10, 6))

plt.plot(df_filtered["threads"], df_filtered["time"], marker="o", label="N=10000, T=1000000")

plt.title("OpenMP: Execution Time VS Threads (N=10.000, T=1.000.000)")
plt.xlabel("Number of threads")
plt.ylabel("Execution time (s)")
plt.grid(True)
plt.legend()
plt.xticks(sorted(df["threads"].unique()))
plt.tight_layout()
plt.show()