import pandas as pd
import matplotlib.pyplot as plt


# Caricamento dati
seq_df = pd.read_csv("../codes_and_jobs/seq_out_results.csv", header=None, names=["N", "T", "Time"])
omp_df = pd.read_csv("../codes_and_jobs/omp_out_results.csv", header=None, names=["N", "T", "Time", "Threads"])
mpi_df = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", header=None, names=["N", "T", "Time", "Processes"])

# seq_grouped = seq_df.groupby(["N", "T"]).mean().reset_index()
# omp_grouped2 = omp_df[omp_df["Threads"] == 2].groupby(["N", "T"]).mean().reset_index()
# mpi_grouped2 = mpi_df[mpi_df["Processes"] == 2].groupby(["N", "T"]).mean().reset_index()
# omp_grouped4 = omp_df[omp_df["Threads"] == 4].groupby(["N", "T"]).mean().reset_index()
# mpi_grouped4 = mpi_df[mpi_df["Processes"] == 4].groupby(["N", "T"]).mean().reset_index()
# omp_grouped8 = omp_df[omp_df["Threads"] == 8].groupby(["N", "T"]).mean().reset_index()
# mpi_grouped8 = mpi_df[mpi_df["Processes"] == 8].groupby(["N", "T"]).mean().reset_index()

# def make_labels(df):
#     return df[["N", "T"]].astype(str).agg("x".join, axis=1)

# labels = make_labels(seq_grouped)
# x = range(len(labels))
# bar_width = 0.25

# plt.figure(figsize=(14, 6))
# plt.bar([i - bar_width for i in x], seq_grouped["Time"], width=bar_width, label="Sequential")
# plt.bar(x, omp_grouped2["Time"], width=bar_width, label="OMP (2 threads)")
# plt.bar(x, omp_grouped8["Time"], width=bar_width, label="OMP (8 threads)")
# plt.bar(x, omp_grouped4["Time"], width=bar_width, label="OMP (4 threads)")
# plt.bar([i + bar_width for i in x], mpi_grouped2["Time"], width=bar_width, label="MPI (2 processes)")
# plt.bar([i + bar_width for i in x], mpi_grouped4["Time"], width=bar_width, label="MPI (4 processes)")
# plt.bar([i + bar_width for i in x], mpi_grouped8["Time"], width=bar_width, label="MPI (8 processes)")


# plt.xticks(x, labels, rotation=45)
# plt.xlabel("N x T")
# plt.ylabel("Execution time (s)")
# plt.title("Execution Time Comparison: Sequential vs OMP vs MPI")
# plt.legend()
# plt.grid(True, axis='y')
# plt.tight_layout()
# plt.show()


seq_grouped = seq_df.groupby(["N", "T"]).mean().reset_index()
omp_grouped2 = omp_df[omp_df["Threads"] == 2].groupby(["N", "T"]).mean().reset_index()
omp_grouped4 = omp_df[omp_df["Threads"] == 4].groupby(["N", "T"]).mean().reset_index()
omp_grouped8 = omp_df[omp_df["Threads"] == 8].groupby(["N", "T"]).mean().reset_index()
mpi_grouped2 = mpi_df[mpi_df["Processes"] == 2].groupby(["N", "T"]).mean().reset_index()
mpi_grouped4 = mpi_df[mpi_df["Processes"] == 4].groupby(["N", "T"]).mean().reset_index()
mpi_grouped8 = mpi_df[mpi_df["Processes"] == 8].groupby(["N", "T"]).mean().reset_index()

def make_labels(df):
    return df[["N", "T"]].astype(str).agg("x".join, axis=1)

labels = make_labels(seq_grouped)
x = list(range(len(labels)))
bar_width = 0.1

split_point = 4 
indexes_1 = x[:split_point]
indexes_2 = x[split_point:]
labels_1 = labels[:split_point]
labels_2 = labels[split_point:]

def plot_execution_time(indexes, labels_subset, title):
    plt.figure(figsize=(14, 6))
    
    plt.bar([i - 3*bar_width for i in indexes], seq_grouped.loc[indexes, "Time"], width=bar_width, label="Sequential")
    plt.bar([i - 2*bar_width for i in indexes], omp_grouped2.loc[indexes, "Time"], width=bar_width, label="OMP (2 threads)")
    plt.bar([i - 1*bar_width for i in indexes], omp_grouped4.loc[indexes, "Time"], width=bar_width, label="OMP (4 threads)")
    plt.bar([i + 0*bar_width for i in indexes], omp_grouped8.loc[indexes, "Time"], width=bar_width, label="OMP (8 threads)")
    plt.bar([i + 1*bar_width for i in indexes], mpi_grouped2.loc[indexes, "Time"], width=bar_width, label="MPI (2 processes)")
    plt.bar([i + 2*bar_width for i in indexes], mpi_grouped4.loc[indexes, "Time"], width=bar_width, label="MPI (4 processes)")
    plt.bar([i + 3*bar_width for i in indexes], mpi_grouped8.loc[indexes, "Time"], width=bar_width, label="MPI (8 processes)")
    
    plt.xticks(indexes, labels_subset, rotation=45)
    plt.xlabel("N x T")
    plt.ylabel("Execution time (s)")
    plt.title(title)
    plt.legend()
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()

plot_execution_time(indexes_1, labels_1, "Execution Time (First 4 couples of N x T)")

plot_execution_time(indexes_2, labels_2, "Execution Time (Last 5 couples of N x T)")




# 16 and 32 procs/threads

seq_df = pd.read_csv("../codes_and_jobs/seq_out_results.csv", header=None, names=["N", "T", "Time"])
omp_df = pd.read_csv("../codes_and_jobs/omp_out_results.csv", header=None, names=["N", "T", "Time", "Threads"])
mpi_df = pd.read_csv("../codes_and_jobs/mpi_out_results.csv", header=None, names=["N", "T", "Time", "Processes"])


seq_grouped = seq_df.groupby(["N", "T"]).mean().reset_index()
omp_grouped16 = omp_df[omp_df["Threads"] == 16].groupby(["N", "T"]).mean().reset_index()
omp_grouped32 = omp_df[omp_df["Threads"] == 32].groupby(["N", "T"]).mean().reset_index()
mpi_grouped16 = mpi_df[mpi_df["Processes"] == 16].groupby(["N", "T"]).mean().reset_index()
mpi_grouped32 = mpi_df[mpi_df["Processes"] == 32].groupby(["N", "T"]).mean().reset_index()

def make_labels(df):
    return df[["N", "T"]].astype(str).agg("x".join, axis=1)

labels = make_labels(seq_grouped)
x = list(range(len(labels)))
bar_width = 0.1

split_point = 4 
indexes_1 = x[:split_point]
indexes_2 = x[split_point:]
labels_1 = labels[:split_point]
labels_2 = labels[split_point:]

def plot_execution_time(indexes, labels_subset, title):
    plt.figure(figsize=(14, 6))
    
    plt.bar([i - 3*bar_width for i in indexes], seq_grouped.loc[indexes, "Time"], width=bar_width, label="Sequential")
    plt.bar([i - 2*bar_width for i in indexes], omp_grouped16.loc[indexes, "Time"], width=bar_width, label="OMP (16 threads)")
    plt.bar([i - 1*bar_width for i in indexes], omp_grouped32.loc[indexes, "Time"], width=bar_width, label="OMP (32 threads)")
    plt.bar([i + 1*bar_width for i in indexes], mpi_grouped16.loc[indexes, "Time"], width=bar_width, label="MPI (16 processes)")
    plt.bar([i + 2*bar_width for i in indexes], mpi_grouped32.loc[indexes, "Time"], width=bar_width, label="MPI (32 processes)")
    
    plt.xticks(indexes, labels_subset, rotation=45)
    plt.xlabel("N x T")
    plt.ylabel("Execution time (s)")
    plt.title(title)
    plt.legend()
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()

plot_execution_time(indexes_1, labels_1, "Execution Time (First 4 couples of N x T)")

plot_execution_time(indexes_2, labels_2, "Execution Time (Last 5 couples of N x T)")