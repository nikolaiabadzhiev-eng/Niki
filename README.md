# My first project
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Параметри на ракетата
g = 9.81   # гравитация (m/s^2)
thrust = 30.0 # тласък (N)
mass = 2.0    # маса (kg)
burn_time = 3 # време на горене (sec)
dt = 0.01     # времеви интервал (sec)
time = np.arange(0, 6, dt)

velocity = []
height = []
v = 0
h = 0

for t in time:
    if t < burn_time:
        a = (thrust/mass) - g
    else:
        a = -g
    v = v + a*dt
    h = h + v*dt
    velocity.append(v)
    height.append(h)

plt.plot(time, height)
plt.title("Височина на ракетата във времето")
plt.xlabel("Време (секунди)")
plt.ylabel("Височина (метри)")
plt.grid()

# Добавяне на ракета като изображение/фигура
ax = plt.gca()
# Местоположение на ракетата - в края на излитането
rocket_x = time[-1]
rocket_y = height[-1]

# Тяло на ракетата (овал)
body = patches.FancyBboxPatch(
    (rocket_x-0.2, rocket_y-2), 0.4, 2,
    boxstyle="round,pad=0.1",
    linewidth=1, edgecolor='black', facecolor='gray', zorder=5)

# Връх на ракетата (триъгълник)
nose = patches.Polygon([
    [rocket_x, rocket_y],
    [rocket_x-0.2, rocket_y-0.2],
    [rocket_x+0.2, rocket_y-0.2]
], closed=True, color='red', zorder=6)

# Дюзи (малък правоъгълник)
nozzle = patches.Rectangle(
    (rocket_x-0.08, rocket_y-2.0), 0.16, 0.2,
    linewidth=1, edgecolor='black', facecolor='orange', zorder=5)

ax.add_patch(body)
ax.add_patch(nose)
ax.add_patch(nozzle)

plt.show()
