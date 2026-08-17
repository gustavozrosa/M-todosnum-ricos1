import numpy as np

# Função
def f(x):
    return 1 - np.exp(-x)

# Limites
a = 0
b = 4

# Número de subintervalos
n = 793

# Regra do Trapézio Múltipla
h = (b - a) / n
x = np.linspace(a, b, n + 1)

I = h * (f(x[0]) + 2 * np.sum(f(x[1:n])) + f(x[n])) / 2

print(f"Integral = {I:.6f}")