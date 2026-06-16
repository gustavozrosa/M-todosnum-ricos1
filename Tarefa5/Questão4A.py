import numpy as np
import pandas as pd

# ===== Dados de entrada =====
date = {
    'x': [1.0, 2.0, 2.5, 3.0, 4.0, 5.0],
    'y': [0.0, 5.0, 6.5, 7.0, 3.0, 1.0]
}

df = pd.DataFrame(date)

# ===== Valor desejado =====
x_desejado = 3.4

# ===== Função das diferenças divididas =====
def diferencas_divididas(x, y):
    n = len(x)
    coef = np.array(y, dtype=float)

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])

    return coef

# ===== Função para calcular o polinômio de Newton =====
def newton(x, coef, x_desejado):
    n = len(coef)
    resultado = coef[n-1]

    for i in range(n-2, -1, -1):
        resultado = resultado * (x_desejado - x[i]) + coef[i]

    return resultado

# ===== Primeiro grau =====
x1 = np.array([3.0, 4.0])
y1 = np.array([7.0, 3.0])

coef1 = diferencas_divididas(x1, y1)
f1 = newton(x1, coef1, x_desejado)

# ===== Segundo grau =====
x2 = np.array([2.5, 3.0, 4.0])
y2 = np.array([6.5, 7.0, 3.0])

coef2 = diferencas_divididas(x2, y2)
f2 = newton(x2, coef2, x_desejado)

# ===== Terceiro grau =====
x3 = np.array([2.0, 2.5, 3.0, 4.0])
y3 = np.array([5.0, 6.5, 7.0, 3.0])

coef3 = diferencas_divididas(x3, y3)
f3 = newton(x3, coef3, x_desejado)

# ===== Resultados =====
print("Newton 1º grau:")
print("Coeficientes =", coef1)
print("f(3.4) =", f1)

print("\nNewton 2º grau:")
print("Coeficientes =", coef2)
print("f(3.4) =", f2)

print("\nNewton 3º grau:")
print("Coeficientes =", coef3)
print("f(3.4) =", f3)