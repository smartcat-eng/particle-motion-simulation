import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

fieldX = []
fieldY = []
inwardFeild = np.linspace(-10, 10, 20)

for i in inwardFeild:
    for j in inwardFeild:
        fieldX.append(i)
        fieldY.append(j)
        

ax.plot(fieldX, fieldY, 'x', color = 'grey')
ax.set_aspect('equal', adjustable='box')

particle, = ax.plot([0], [0], 'or')

t = np.linspace(0, 2 * np.pi, 500)

B =2
v =5
q =1
m =1
w =(q*B)/m
p = (m * v)/(q * B)

def update(frame):
    particle.set_xdata([p * np.sin(w * frame)])
    particle.set_ydata([p * np.cos(w * frame)])
    return particle,

ani = FuncAnimation(fig, update, frames=t, interval = 30)

plt.show()