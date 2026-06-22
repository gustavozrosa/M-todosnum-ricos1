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

# ===== Função das Diferenças Divididas de Newton =====
def diferencas_divididas(x, y):
    n = len(x)
    coef = np.array(y, dtype=float)

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])

    return coef

# ===== Função para Calcular o Polinômio de Newton =====
def newton(x, coef, x_desejado):
    n = len(coef)
    resultado = coef[n-1]

    for i in range(n-2, -1, -1):
        resultado = resultado * (x_desejado - x[i]) + coef[i]

    return resultado

# ===== Aplicando o Método de Newton =====
x = np.array(df['x'])
y = np.array(df['y'])

coef = diferencas_divididas(x, y)

print("Coeficientes das diferenças divididas:")
print(coef)

# ===== Calculando y em x = 3.5 =====
y_desejado = newton(x, coef, x_desejado)

print("\nValor interpolado:")
print("y(3.5) =", y_desejado)

# ===== Verificação nos pontos da tabela =====
y_verificado = np.zeros(len(x))

for i in range(len(x)):
    y_verificado[i] = newton(x, coef, x[i])

erro = y - y_verificado

print("\nValores verificados pelo polinômio:")
print(y_verificado)

print("\nErro nos pontos da tabela:")
print(erro)

# ===== Gráfico =====
x_plot = np.linspace(min(x), max(x), 200)

y_plot = np.zeros(len(x_plot))

for i in range(len(x_plot)):
    y_plot[i] = newton(x, coef, x_plot[i])

plt.plot(df['x'], df['y'], 'or', label='Dados da Tabela')
plt.plot(x_plot, y_plot, '-b', label='Polinômio de Newton')
plt.plot(x_desejado, y_desejado, 'ok', label='y(3.5)')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolação Polinomial de Newton')
plt.grid(True)
plt.show()