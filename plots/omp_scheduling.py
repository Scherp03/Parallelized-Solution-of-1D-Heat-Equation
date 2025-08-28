import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('omp_schedule_results.csv')

df_min = df.groupby(['schedule', 'threads'], as_index=False)['time'].min()

plt.figure(figsize=(10, 6))

thread_vals = sorted(df_min['threads'].unique())

for schedule_type in df_min['schedule'].unique():
    subset = df_min[df_min['schedule'] == schedule_type]
    y_vals = [subset[subset['threads'] == t]['time'].values[0] if t in subset['threads'].values else None for t in thread_vals]
    plt.plot(thread_vals, y_vals, marker='o', label=schedule_type)

plt.xticks(thread_vals)
plt.xlabel('Number of Threads')
plt.ylabel('Minimum Execution Time (s)')
plt.title('Best Execution Time For each OMP Scheduling')
plt.legend(title='Schedule')
plt.grid(True)
plt.tight_layout()
plt.show()
