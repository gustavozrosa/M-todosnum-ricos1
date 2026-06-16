import numpy as np
import matplotlib.pyplot as plt

def y1(x):
    return -x**2 + x + 0.5

def y2(x):
    return x**2/(1 + 5*x)

x = np.linspace(-1, 2, 1000)

# Evita problema perto de x = -0.2, onde o denominador zera
x = x[x != -0.2]

plt.plot(x, y1(x), label="y = -x² + x + 0.5")
plt.plot(x, y2(x), label="y = x²/(1 + 5x)")

plt.axhline(0)
plt.axvline(0)

plt.ylim(-2, 2)
plt.grid()
plt.legend()
plt.title("Solução gráfica do sistema não linear")
plt.xlabel("x")
plt.ylabel("y")

plt.show()