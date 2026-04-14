import numpy as np
import matplotlib.pyplot as plt

# ------------------------
# 1) FUNÇÃO E DERIVADA
# ------------------------

def f(x):
    return np.sin(4*x) + np.cos(5*x) + 1/x

def df(x):
    return 4*np.cos(4*x) - 5*np.sin(5*x) - 1/x**2

# ------------------------
# 2) GRÁFICO
# ------------------------

x = np.linspace(0.1, 2*np.pi, 1000)
y = f(x)

plt.plot(x, y)
plt.axhline(0)
plt.grid()
plt.show()

# ------------------------
# 3) BUSCA INCREMENTAL
# ------------------------

print("\nBUSCA INCREMENTAL:")

x = 0.1
passo = 0.01

intervalos = []

while x < 2*np.pi:
    if f(x) * f(x + passo) < 0:
        print("Raiz entre:", x, "e", x + passo)
        intervalos.append((x, x + passo))
    x = x + passo

# ------------------------
# 4) CRITÉRIO DE PARADA
# ------------------------

eppara = 0.5 * 10**(-4)

# ------------------------
# 5) MÉTODOS PARA CADA RAIZ
# ------------------------

for i, (a, b) in enumerate(intervalos):
    
    print("\n========================")
    print("RAIZ", i + 1)
    print("Intervalo:", a, "a", b)

    # ------------------------
    # BISSECÇÃO
    # ------------------------

    xl = a
    xu = b
    epest = 100
    xr_old = 0

    while epest > eppara:
        xr = (xl + xu) / 2

        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr

        epest = abs((xr - xr_old) / xr) * 100
        xr_old = xr

    print("BISSECÇÃO:", xr)

    # ------------------------
    # FALSA POSIÇÃO
    # ------------------------

    xl = a
    xu = b
    epest = 100
    xr_old = 0

    while epest > eppara:
        xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))

        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr

        epest = abs((xr - xr_old) / xr) * 100
        xr_old = xr

    print("FALSA POSIÇÃO:", xr)

    # ------------------------
    # NEWTON-RAPHSON
    # ------------------------

    x = (a + b) / 2
    epest = 100

    while epest > eppara:
        xnovo = x - f(x) / df(x)
        epest = abs((xnovo - x) / xnovo) * 100
        x = xnovo

    print("NEWTON-RAPHSON:", x)

    # ------------------------
    # SECANTE
    # ------------------------

    x0 = a
    x1 = b
    epest = 100

    while epest > eppara:
        x2 = x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        epest = abs((x2 - x1) / x2) * 100
        x0 = x1
        x1 = x2

    print("SECANTE:", x2)

    # ------------------------
    # SECANTE MODIFICADA
    # ------------------------

    x = (a + b) / 2
    delta = 0.01
    epest = 100

    while epest > eppara:
        xnovo = x - (delta * x * f(x)) / (f(x + delta * x) - f(x))
        epest = abs((xnovo - x) / xnovo) * 100
        x = xnovo

    print("SECANTE MODIFICADA:", x)