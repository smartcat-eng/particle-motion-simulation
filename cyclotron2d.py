import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', adjustable='box')

fieldX = []
fieldY = []
inwardFeild = np.linspace(-10, 10, 20)

for i in inwardFeild:
    for j in inwardFeild:
        fieldX.append(i)
        fieldY.append(j)
        

ax.plot(fieldX, fieldY, 'x', color = 'grey')

particle, = ax.plot([0], [0], 'or')
velVector = ax.quiver([100], [100], [5], [0], scale_units = 'xy', angles = 'xy', scale = 1, color = "blue")
fVector = ax.quiver([100], [100], [5], [0], scale_units = 'xy', angles = 'xy', scale = 1, color = "green")

time = np.linspace(0, 2 * np.pi, 500)

B =2
v =5
q =3
m =2
w =(q*B)/m
p = (m * v)/(q * B)

startX = 5
startY = 3

centerX = startX - (p * np.sin(0))
centerY = startY - (p * np.cos(0))
ax.plot(centerX, centerY, 'x', color = "purple", ms = 10)

pathX = (p * np.cos(time)) + centerX
pathY = (p * np.sin(time)) + centerY
ax.plot(pathX, pathY, '--', color = "black")



def update(frame):
    posX = [(p * np.sin(w * frame)) + centerX]
    posY = [p * np.cos(w * frame) + centerY]
    particle.set_xdata(posX)
    particle.set_ydata(posY)

    velVector.set_offsets(np.column_stack((posX, posY)))

    velX = [v * np.cos(w * frame)]
    velY = [v * -1 * np.sin(w * frame)]
    velVector.set_UVC(velX, velY)

    fVector.set_offsets(np.column_stack((posX, posY)))

    fX = m * v * -1 * w * np.sin(w * frame)
    fY = m * v * -1 * w * np.cos(w * frame)
    fVector.set_UVC(fX, fY)

    return particle, velVector, fVector

ani = FuncAnimation(fig, update, frames=time, interval = 30)

plt.show()