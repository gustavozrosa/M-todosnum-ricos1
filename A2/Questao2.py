import numpy as np
import matplotlib.pyplot as plt

# ------------------------
# 1) FUNÇÃO
# ------------------------

def f(x):
    return np.sin(x) + np.cos(1 + x**2) - 1

# ------------------------
# 2) GRÁFICO
# ------------------------

x = np.linspace(0, 4, 1000)
y = f(x)

plt.plot(x, y)
plt.axhline(0)
plt.grid()
plt.show()

# ------------------------
# 3) CRITÉRIO DE PARADA
# ------------------------

eppara = 0.5 * 10**(-4)

# ------------------------
# 4) MÉTODO DA SECANTE
# ------------------------

print("\nCASO A")
x0 = 1.0
x1 = 3.0
epest = 100

while epest > eppara:
    x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
    epest = abs((x2 - x1) / x2) * 100
    x0 = x1
    x1 = x2

print("Raiz =", x2)

print("\nCASO B")
x0 = 1.5
x1 = 2.5
epest = 100

while epest > eppara:
    x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
    epest = abs((x2 - x1) / x2) * 100
    x0 = x1
    x1 = x2

print("Raiz =", x2)

print("\nCASO C")
x0 = 1.5
x1 = 2.25
epest = 100

while epest > eppara:
    x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
    epest = abs((x2 - x1) / x2) * 100
    x0 = x1
    x1 = x2

print("Raiz =", x2)