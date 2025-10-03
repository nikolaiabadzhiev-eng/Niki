# My first project
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Параметри на колата
g = 9.81          # гравитация (m/s^2)
engine_force = 20 # сила от двигателя (N)
mass = 1.5        # маса на колата (kg)
friction = 0.5    # коефициент на триене
dt = 0.01         # времеви интервал (sec)
time = np.arange(0, 10, dt)

velocity = []
distance = []
v = 0
d = 0

for t in time:
    # Сила на триене
    friction_force = friction * mass * g
    # Сумарна сила
    net_force = engine_force - friction_force if engine_force > friction_force else 0
    a = net_force / mass
    v = v + a * dt
    d = d + v * dt
    velocity.append(v)
    distance.append(d)

plt.plot(time, distance)
plt.title("Изминато разстояние от колата във времето")
plt.xlabel("Време (секунди)")
plt.ylabel("Разстояние (метри)")
plt.grid()

# Добавяне на кола като изображение/фигура
ax = plt.gca()
# Местоположение на колата - в края на движението
car_x = time[-1]
car_y = distance[-1]

# Тяло на колата (правоъгълник)
body = patches.Rectangle(
    (car_x-1, car_y-0.3), 2, 0.6,
    linewidth=1, edgecolor='black', facecolor='blue', zorder=5)

# Гуми на колата (кръгове)
wheel1 = patches.Circle((car_x-0.7, car_y-0.3), 0.25, color='black', zorder=6)
wheel2 = patches.Circle((car_x+0.7, car_y-0.3), 0.25, color='black', zorder=6)

# Предно стъкло (триъгълник)
window = patches.Polygon([
    [car_x-0.3, car_y+0.3],
    [car_x, car_y+0.6],
    [car_x+0.3, car_y+0.3]
], closed=True, color='lightblue', zorder=7)

ax.add_patch(body)
ax.add_patch(wheel1)
ax.add_patch(wheel2)
ax.add_patch(window)

plt.show()
