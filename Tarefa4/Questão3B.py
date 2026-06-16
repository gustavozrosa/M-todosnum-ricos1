import numpy as np
import matplotlib.pyplot as plt

def F(x):
    x1 = x[0]
    x2 = x[1]

    return np.array([
        x2 + x1**2 - x1 - 0.5,
        x2 + 5*x1*x2 - x1**2
    ])

def J(x):
    x1 = x[0]
    x2 = x[1]

    return np.array([
        [2*x1 - 1, 1],
        [5*x2 - 2*x1, 1 + 5*x1]
    ])

# chutes iniciais
chutes = [
    np.array([1.0, 0.2]),
    np.array([-0.5, -0.1]),
    np.array([-0.1, 0.3])
]

Eppara = 0.5 * 10**(-4)

solucoes = []

for x in chutes:

    Epest = 100
    k = 0

    while Epest > Eppara:

        delta = np.linalg.solve(J(x), -F(x))

        x_novo = x + delta

        Epest = np.max(abs((x_novo - x) / x_novo)) * 100

        x = x_novo
        k = k + 1

    solucoes.append(x)

    print("Solução final:")
    print("x =", x[0])
    print("y =", x[1])
    print("Número de iterações:", k)
    print()

# gráfico
def y1(x):
    return -x**2 + x + 0.5

def y2(x):
    return x**2/(1 + 5*x)

xx = np.linspace(-1, 2, 1000)

xx1 = np.linspace(-1, -0.21, 500)
xx2 = np.linspace(-0.19, 2, 500)

plt.plot(xx, y1(xx), label="y = -x² + x + 0.5")
plt.plot(xx1, y2(xx1), label="y = x²/(1 + 5x)")
plt.plot(xx2, y2(xx2))

# pontos das soluções
for s in solucoes:
    plt.plot(s[0], s[1], "ro")

plt.ylim(-0.5, 0.5)
plt.grid()
plt.legend()
plt.title("Newton-Raphson para sistema não linear")
plt.xlabel("x")
plt.ylabel("y")

plt.show()