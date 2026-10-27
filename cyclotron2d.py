import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
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
v =5
q =-1
m =1
w =abs(q*B)/m
p = (m * v)/abs(q * B)
rotationNum = 10
sign = np.sign(q)

time = np.linspace(0, rotationNum * 2 * np.pi / w, abs(round(1500 / rotationNum * w)))

startX = -5
startY = 3

initVel = ax.quiver([startX], [startY], [v * np.cos(angle)], [v * np.sin(angle)], scale_units = 'xy', angles = 'xy', scale = 1)

centerX = startX - (sign * p * np.sin(angle))
centerY = startY - (sign * -p * np.cos(angle))
ax.plot(centerX, centerY, 'x', color = "purple", ms = 10)

pathX = (p * np.cos(np.linspace(0, 2 * np.pi, 200))) + centerX
pathY = (p * np.sin(np.linspace(0, 2 * np.pi, 200))) + centerY
ax.plot(pathX, pathY, '--', color = "black")



def update(frame):
    posX = [(p * np.sin((w * frame * sign) + angle)) + centerX]
    posY = [-p * np.cos((w * frame * sign) + angle) + centerY]
    particle.set_xdata(posX)
    particle.set_ydata(posY)

    velVector.set_offsets(np.column_stack((posX, posY)))

    velX = [sign * v * np.cos((w * frame * sign) + angle)]
    velY = [sign * v * np.sin((w * frame * sign) + angle)]
    velVector.set_UVC(velX, velY)

    fVector.set_offsets(np.column_stack((posX, posY)))

    fX = m * -v * w * np.sin((w * frame * sign) + angle)
    fY = m * v * w * np.cos((w * frame * sign) + angle)
    fVector.set_UVC(fX, fY)

    return particle, velVector, fVector

ani = FuncAnimation(fig, update, frames=time, interval = 30)

plt.show()