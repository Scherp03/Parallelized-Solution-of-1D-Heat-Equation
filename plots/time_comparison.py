# import pandas as pd
# import matplotlib.pyplot as plt


# seq_df = pd.read_csv("../codes_and_jobs/seq_out_results.csv", header=None, names=["N", "T", "Time"])
# omp_df = pd.read_csv("../codes_and_jobs/omp_out_results.csv", header=None, names=["N", "T", "Time", "Threads"])
# mpi_df = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", header=None, names=["N", "T", "Time", "Processes"])

# parallel_levels = [2, 4, 8, 16, 32]
# T_list = [10000, 100000]
# bar_width = 0.06


# seq_grouped = seq_df.groupby(["N", "T"]).mean().reset_index()
# omp_grouped = omp_df[omp_df["Threads"].isin(parallel_levels)].groupby(["N", "T", "Threads"]).mean().reset_index()
# mpi_grouped = mpi_df[mpi_df["Processes"].isin(parallel_levels)].groupby(["N", "T", "Processes"]).mean().reset_index()


# for T_val in T_list:
#     seq_t = seq_grouped[seq_grouped["T"] == T_val]
#     omp_t = omp_grouped[omp_grouped["T"] == T_val]
#     mpi_t = mpi_grouped[mpi_grouped["T"] == T_val]

#     Ns = seq_t["N"].tolist()
#     x = list(range(len(Ns)))
#     offset = -5 * bar_width

#     plt.figure(figsize=(18, 6))

#     # Sequential
#     plt.bar([i + offset for i in x], seq_t["Time"], width=bar_width, label="Sequential")
#     offset += bar_width

#     # OMP
#     for threads in parallel_levels:
#         omp_sub = omp_t[omp_t["Threads"] == threads].set_index("N").reindex(Ns).reset_index()
#         plt.bar([i + offset for i in x], omp_sub["Time"], width=bar_width, label=f"OMP ({threads} threads)")
#         offset += bar_width

#     # MPI
#     for procs in parallel_levels:
#         mpi_sub = mpi_t[mpi_t["Processes"] == procs].set_index("N").reindex(Ns).reset_index()
#         plt.bar([i + offset for i in x], mpi_sub["Time"], width=bar_width, label=f"MPI ({procs} processes)")
#         offset += bar_width


#     plt.xticks(x, [str(n) for n in Ns], rotation=45)
#     plt.xlabel("N (con T = {})".format(T_val))
#     plt.ylabel("Execution time (s)")
#     plt.title(f"Execution Time Comparison for N (T = {T_val})")
#     plt.legend(ncol=2)
#     plt.grid(True, axis='y')
#     plt.tight_layout()
#     plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt

# seq_df = pd.read_csv("../codes_and_jobs/seq_out_results.csv", header=None, names=["N", "T", "Time"])
# omp_df = pd.read_csv("../codes_and_jobs/omp_out_results.csv", header=None, names=["N", "T", "Time", "Threads"])
# mpi_df = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", header=None, names=["N", "T", "Time", "Processes"])

# parallel_levels = [2, 4, 8, 16, 32]

# seq_grouped = seq_df.groupby(["N", "T"]).mean().reset_index()
# omp_grouped = omp_df[omp_df["Threads"].isin(parallel_levels)].groupby(["N", "T", "Threads"]).mean().reset_index()
# mpi_grouped = mpi_df[mpi_df["Processes"].isin(parallel_levels)].groupby(["N", "T", "Processes"]).mean().reset_index()

# unique_N = sorted(seq_grouped["N"].unique())
# bar_width = 0.06

# for n_val in unique_N:
#     seq_n = seq_grouped[seq_grouped["N"] == n_val]
#     omp_n = omp_grouped[omp_grouped["N"] == n_val]
#     mpi_n = mpi_grouped[mpi_grouped["N"] == n_val]

#     labels = seq_n["T"].astype(str).tolist()
#     x = list(range(len(labels)))

#     plt.figure(figsize=(12, 6))

#     offset = -5 * bar_width  

#     # Sequential
#     plt.bar([i + offset for i in x], seq_n["Time"], width=bar_width, label="Sequential")
#     offset += bar_width

#     # OMP 
#     for threads in parallel_levels:
#         omp_t = omp_n[omp_n["Threads"] == threads].set_index("T").reindex(seq_n["T"]).reset_index()
#         plt.bar([i + offset for i in x], omp_t["Time"], width=bar_width, label=f"OMP ({threads} threads)")
#         offset += bar_width

#     # MPI 
#     for procs in parallel_levels:
#         mpi_t = mpi_n[mpi_n["Processes"] == procs].set_index("T").reindex(seq_n["T"]).reset_index()
#         plt.bar([i + offset for i in x], mpi_t["Time"], width=bar_width, label=f"MPI ({procs} processes)")
#         offset += bar_width

#     plt.xticks(x, labels, rotation=45)
#     plt.xlabel(f"T")
#     plt.ylabel("Execution time (s)")
#     plt.title(f"Execution Time Comparison for T (N = {n_val})")
#     plt.legend(ncol=2)
#     plt.grid(True, axis='y')
#     plt.tight_layout()
#     plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Caricamento dati
seq_df = pd.read_csv("../codes_and_jobs/seq_out_results.csv", header=None, names=["N", "T", "Time"])
omp_df = pd.read_csv("../codes_and_jobs/omp_out_results.csv", header=None, names=["N", "T", "Time", "Threads"])
mpi_df = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", header=None, names=["N", "T", "Time", "Processes"])

parallel_levels = [2, 4, 8, 16, 32]

# Raggruppamento e filtro per T = 100000
seq_grouped = seq_df[seq_df["T"] == 100000].groupby(["N", "T"]).mean().reset_index()
omp_grouped = omp_df[(omp_df["T"] == 100000) & (omp_df["Threads"].isin(parallel_levels))].groupby(["N", "T", "Threads"]).mean().reset_index()
mpi_grouped = mpi_df[(mpi_df["T"] == 100000) & (mpi_df["Processes"].isin(parallel_levels))].groupby(["N", "T", "Processes"]).mean().reset_index()

unique_N = sorted(seq_grouped["N"].unique())
bar_width = 0.06

for n_val in unique_N:
    seq_n = seq_grouped[seq_grouped["N"] == n_val]
    omp_n = omp_grouped[omp_grouped["N"] == n_val]
    mpi_n = mpi_grouped[mpi_grouped["N"] == n_val]

    labels = ["T = 100000"]
    x = [0]

    plt.figure(figsize=(8, 6))

    offset = -5 * bar_width

    # Sequential
    plt.bar([i + offset for i in x], seq_n["Time"], width=bar_width, label="Sequential")
    offset += bar_width

    # OMP
    for threads in parallel_levels:
        omp_t = omp_n[omp_n["Threads"] == threads]
        plt.bar([i + offset for i in x], omp_t["Time"], width=bar_width, label=f"OMP ({threads} threads)")
        offset += bar_width

    # MPI
    for procs in parallel_levels:
        mpi_t = mpi_n[mpi_n["Processes"] == procs]
        plt.bar([i + offset for i in x], mpi_t["Time"], width=bar_width, label=f"MPI ({procs} processes)")
        offset += bar_width

    plt.xticks(x, labels)
    plt.xlabel("T")
    plt.ylabel("Execution time (s)")
    plt.title(f"Execution Time Comparison at T = 100000 (N = {n_val})")
    plt.legend(ncol=2)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()
