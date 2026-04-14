import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(4*x) + np.cos(5*x) + 1/x

x = np.linspace(0.1, 2*np.pi, 1000)
y = f(x)

plt.plot(x, y)
plt.axhline(0)
plt.grid()
plt.show()

x = 0.1
passo = 0.01

while x < 2*np.pi:
    if f(x) * f(x + passo) < 0:
        print("Raiz entre:", x, "e", x + passo)
    x = x + passo