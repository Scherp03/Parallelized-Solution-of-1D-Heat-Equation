import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt(".csv", delimiter=",")

x = data[:, 0]  
u = data[:, 1] 

plt.plot(x, u, label="Temperature")
plt.xlabel("x (along rod)")
plt.ylabel("u(x)")
plt.title("Final temperature distribution")
plt.grid(True)
plt.legend()
plt.show()