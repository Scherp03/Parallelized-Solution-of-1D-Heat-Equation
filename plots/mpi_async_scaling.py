import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../MPI_async/mpi_async_out_results.csv", header=None, names=["N", "T", "time", "procs"])

df.sort_values(by=["N", "T", "procs"], inplace=True)

grouped = df.groupby(["N", "T"])

plt.figure(figsize=(10, 6))

for (n, t), group in grouped:
    label = f"N={n}, T={t}"
    plt.plot(group["procs"], group["time"], marker="o", label=label)

plt.title("MPI Time vs procs")
plt.xlabel("Number of procs")
plt.ylabel("Execution time (s)")
plt.grid(True)
plt.legend()
plt.xticks(sorted(df["procs"].unique()))
plt.tight_layout()
plt.show()


# only small values

filtered_df = df[df["N"].isin([100000, 1000000, 500000, 5000000]) & df["T"].isin([100000, 10000])]

exclude_pairs = [(5000000, 100000), (5000000, 1000000), (1000000, 1000000), (1000000, 100000)]
for n, t in exclude_pairs:
    filtered_df = filtered_df[~((filtered_df["N"] == n) & (filtered_df["T"] == t))]

filtered_grouped = filtered_df.groupby(["N", "T"])

plt.figure(figsize=(10, 6))
for (n, t), group in filtered_grouped:
    label = f"N={n}, T={t}"
    plt.plot(group["procs"], group["time"], marker="o", label=label)

plt.title("MPI Time vs procs (only smaller values)")
plt.xlabel("Number of procs")
plt.ylabel("Execution time (s)")
plt.grid(True)
plt.legend()
plt.xticks(sorted(filtered_df["procs"].unique()))
plt.tight_layout()
plt.show()