import matplotlib.pyplot as plt
import numpy as np

# Създаваме фигура и ос
fig, ax = plt.subplots(figsize=(8, 4))

# Цветове на дъгата
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# Рисуваме цветните дъги
for i, color in enumerate(colors):
    radius = 1 + i * 0.15
    arc = plt.Circle((4, 0), radius, color=color, fill=False, linewidth=15)
    ax.add_patch(arc)

ax.set_xlim(-1, 9)
ax.set_ylim(-1, 4)
ax.set_aspect('equal')
plt.axis('off')
plt.title("Цветна дъга")
plt.show()
