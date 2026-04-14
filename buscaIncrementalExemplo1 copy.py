import numpy as np
import math

def f(x):
    return np.sin(10*x) + np.cos(3*x)

# Vetor
n = 100
x = np.linspace(3,6,n)

# Alocação de memória
xb = []
nb = 0

# Busca Incremental
for i in range(n-1):
    xl = x[i]
    xu = x[i+1]

    if (f(xl)*f(xu) < 0):
        nb += 1
        xb.append([xl,xu])
if not xb:
    print("nenhum subintervalo foi encontrado")

print("xb = ", xb)
print("Número de subintervalos = ", nb)

