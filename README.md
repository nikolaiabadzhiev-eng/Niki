# My first project
import matplotlib.pyplot as plt
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
plt.show()
