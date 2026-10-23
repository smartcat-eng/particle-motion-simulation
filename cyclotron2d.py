import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

feildX = []
feildY = []
inwardFeild = np.linspace(-10, 10, 20)

for i in inwardFeild:
    for j in inwardFeild:
        feildX.append(i)
        feildY.append(j)
        

ax.plot(feildX, feildY, 'x', color = 'grey')
ax.set_aspect('equal', adjustable='box')

plt.show()