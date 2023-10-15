import matplotlib.pyplot as plt
import numpy as np

plt.subplot(2, 2, 1)
x1 = np.linspace(-2 * np.pi, 2 * np.pi, 240)
y1 = np.cos(x1)
plt.plot(x1, y1, color='red')
plt.grid(True)
plt.xlabel('График cos(x)', loc='center', fontsize=12)
plt.ylabel('y')
plt.subplot(2, 2, 2)
y2 = np.sin(x1)
plt.plot(x1, y2, color='blue')
plt.grid(True)
plt.xlabel('График sin(x)', loc='center', fontsize=12)
plt.ylabel('y')
plt.subplot(2, 2, 3)
x3 = np.linspace(-8, 8, 100)
y3 = x3 ** 2
plt.plot(x3, y3, color='green')
plt.grid(True)
plt.xlabel('График x^2', loc='center', fontsize=12)
plt.ylabel('y')
plt.subplot(2, 2, 4)
x4_1 = np.linspace(-2, -0.01, 100)
x4_2 = np.linspace(0.01, 2, 100)
y4_1 = 2 / x4_1
y4_2 = 2 / x4_2
plt.plot(x4_1, y4_1,  x4_2, y4_2, color='purple')
plt.grid(True)
plt.xlabel('График 2 / x', loc='center', fontsize=12)
plt.ylabel('y')
plt.show()
