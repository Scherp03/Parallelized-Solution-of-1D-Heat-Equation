import pandas as pd
import matplotlib.pyplot as plt

df_sync = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", header=None)
df_async = pd.read_csv("../MPI_async/mpi_async_out_results.csv", header=None)

columns = ["N", "T", "Execution Time", "procs"]
df_sync.columns = columns
df_async.columns = columns

for N in sorted(df_sync["N"].unique()):
    
    T = df_sync[df_sync["N"] == N]["T"].iloc[0]

    filtered_sync = df_sync[(df_sync["N"] == N) & (df_sync["T"] == T)].sort_values(by="procs")
    filtered_async = df_async[(df_async["N"] == N) & (df_async["T"] == T)].sort_values(by="procs")

    if filtered_sync.empty or filtered_async.empty:
        continue

    plt.figure(figsize=(10, 6))
    plt.plot(filtered_sync["procs"], filtered_sync["Execution Time"], marker='o', label="Sync")
    plt.plot(filtered_async["procs"], filtered_async["Execution Time"], marker='o', label="Async")
    plt.xlabel("Number of processes")
    plt.ylabel("Execution time (s)")
    plt.title(f"MPI Sync vs Async\nN = {N}, T = {T}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()
