import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

# ===== Dados de entrada =====
date = {
    'x': [0.0, 1.8, 5.0, 6.0, 8.2, 9.2, 12.0],
    'y': [26.000, 16.415, 5.375, 3.500, 2.015, 2.540, 8.000]
}

df = pd.DataFrame(date)

# ===== Valor desejado =====
x_desejado = 3.5

# ===== Construindo a Matriz de Vandermonde =====
n = len(df['x'])

A = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        A[i, j] = df['x'][i]**j

b = np.array(df['y'])

# ===== Solução do Sistema Linear =====
ai = np.linalg.solve(A, b)

print("Coeficientes do polinômio:")
print(ai)

# ===== Calculando y em x = 3.5 =====
y_desejado = 0

for i in range(n):
    y_desejado = y_desejado + ai[i] * x_desejado**i

print("\nValor interpolado:")
print("y(3.5) =", y_desejado)

# ===== Verificação nos pontos da tabela =====
y_verificado = np.zeros(n)

for i in range(n):
    for j in range(n):
        y_verificado[i] = y_verificado[i] + ai[j] * df['x'][i]**j

erro = df['y'] - y_verificado

print("\nValores verificados pelo polinômio:")
print(y_verificado)

print("\nErro nos pontos da tabela:")
print(erro)

# ===== Gráfico =====
x_plot = np.linspace(min(df['x']), max(df['x']), 200)

y_plot = np.zeros(len(x_plot))

for i in range(n):
    y_plot = y_plot + ai[i] * x_plot**i

plt.plot(df['x'], df['y'], 'or', label='Dados da Tabela')
plt.plot(x_plot, y_plot, '-b', label='Polinômio Interpolador')
plt.plot(x_desejado, y_desejado, 'ok', label='y(3.5)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()