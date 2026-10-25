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

angle = -np.pi / 3
B =2
v =10
q =3
m =1
w =(q*B)/m
p = (m * v)/(q * B)
rotationNum = 10

time = np.linspace(0, rotationNum * 2 * np.pi / w, round(1000 / rotationNum * w))

startX = 0
startY = 0

initVel = ax.quiver([startX], [startY], [v * np.cos(angle)], [v * np.sin(angle)], scale_units = 'xy', angles = 'xy', scale = 1)

centerX = startX - (p * np.sin(angle))
centerY = startY - (-p * np.cos(angle))
ax.plot(centerX, centerY, 'x', color = "purple", ms = 10)

pathX = (p * np.cos(np.linspace(0, 2 * np.pi, 200))) + centerX
pathY = (p * np.sin(np.linspace(0, 2 * np.pi, 200))) + centerY
ax.plot(pathX, pathY, '--', color = "black")



def update(frame):
    posX = [(p * np.sin((w * frame) + angle)) + centerX]
    posY = [-p * np.cos((w * frame) + angle) + centerY]
    particle.set_xdata(posX)
    particle.set_ydata(posY)

    velVector.set_offsets(np.column_stack((posX, posY)))

    velX = [v * np.cos((w * frame) + angle)]
    velY = [v * np.sin((w * frame) + angle)]
    velVector.set_UVC(velX, velY)

    fVector.set_offsets(np.column_stack((posX, posY)))

    fX = m * -v * w * np.sin((w * frame) + angle)
    fY = m * v * w * np.cos((w * frame) + angle)
    fVector.set_UVC(fX, fY)

    return particle, velVector, fVector

ani = FuncAnimation(fig, update, frames=time, interval = 30)

plt.show()