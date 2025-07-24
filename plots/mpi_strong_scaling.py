import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", header=None, names=["N", "T", "time", "procs"])

df_filtered = df[(df["N"] == 1000) & (df["T"] == 100000)].copy()

df_filtered.sort_values(by="procs", inplace=True)

plt.figure(figsize=(10, 6))

plt.plot(df_filtered["procs"], df_filtered["time"], marker="o", label="N=1000, T=100000")

plt.title("MPI: Execution Time VS Processes (N=1.000, T=100.000)")
plt.xlabel("Number of processes")
plt.ylabel("Execution time (s)")
plt.grid(True)
plt.legend()
plt.xticks(sorted(df["procs"].unique()))
plt.tight_layout()
plt.show()


# N and T different 

df = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", header=None, names=["N", "T", "time", "procs"])

df_filtered = df[(df["N"] == 10000) & (df["T"] == 1000000)].copy()

df_filtered.sort_values(by="procs", inplace=True)

plt.figure(figsize=(10, 6))

plt.plot(df_filtered["procs"], df_filtered["time"], marker="o", label="N=10000, T=1000000")

plt.title("MPI: Execution Time VS Processes (N=10.000, T=1.000.000)")
plt.xlabel("Number of processes")
plt.ylabel("Execution time (s)")
plt.grid(True)
plt.legend()
plt.xticks(sorted(df["procs"].unique()))
plt.tight_layout()
plt.show()