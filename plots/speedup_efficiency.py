import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("speedup_eff_N1000_T100000 .csv")


T1 = df[df["type"] == "seq"]["time"].values[0]
df["speedup"] = T1 / df["time"]
df["efficiency"] = df["speedup"] / df["p"]


df_parallel = df[df["type"] != "seq"]


df_parallel = df_parallel.sort_values(by=["type", "p"])


types = df_parallel["type"].unique()
p_values = sorted(df_parallel["p"].unique())


bar_width = 0.8 / len(types)
x = np.arange(len(p_values))


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



# different N and T


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("speedup_eff_N10000_T500000.csv")


T1 = df[df["type"] == "seq"]["time"].values[0]
df["speedup"] = T1 / df["time"]
df["efficiency"] = df["speedup"] / df["p"]


df_parallel = df[df["type"] != "seq"]


df_parallel = df_parallel.sort_values(by=["type", "p"])


types = df_parallel["type"].unique()
p_values = sorted(df_parallel["p"].unique())


bar_width = 0.8 / len(types)
x = np.arange(len(p_values))


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



# different N and T


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("speedup_eff_N100000_T1000000 .csv")


T1 = df[df["type"] == "seq"]["time"].values[0]
df["speedup"] = T1 / df["time"]
df["efficiency"] = df["speedup"] / df["p"]


df_parallel = df[df["type"] != "seq"]


df_parallel = df_parallel.sort_values(by=["type", "p"])


types = df_parallel["type"].unique()
p_values = sorted(df_parallel["p"].unique())


bar_width = 0.8 / len(types)
x = np.arange(len(p_values))


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

