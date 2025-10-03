import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(6, 4))

# Тяло на колата
body = patches.Rectangle((2, 2), 6, 2, linewidth=2, edgecolor='black', facecolor='blue')
ax.add_patch(body)

# Гуми
wheel1 = patches.Circle((3, 2), 0.7, color='black')
wheel2 = patches.Circle((7, 2), 0.7, color='black')
ax.add_patch(wheel1)
ax.add_patch(wheel2)

# Предно стъкло
window = patches.Polygon([[6, 4], [7, 4], [7, 3], [6, 3]], closed=True, color='lightblue')
ax.add_patch(window)

# Фарове
headlight = patches.Circle((8, 3), 0.2, color='yellow')
ax.add_patch(headlight)

ax.set_xlim(0, 10)
ax.set_ylim(1, 5)
ax.set_aspect('equal')
plt.axis('off')
plt.title("Графично изображение на кола")
plt.show()
