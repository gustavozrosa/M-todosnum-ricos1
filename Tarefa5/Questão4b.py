import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===== Dados de entrada =====
date = {
    'x': [1.0, 2.0, 2.5, 3.0, 4.0, 5.0],
    'y': [0.0, 5.0, 6.5, 7.0, 3.0, 1.0]
}

df = pd.DataFrame(date)

# ===== Valor desejado =====
x_desejado = 3.4

# ===== Função de Lagrange =====
def lagrange(x, y, x_desejado):
    n = len(x)
    resultado = 0

    for i in range(n):
        termo = y[i]

        for j in range(n):
            if i != j:
                termo = termo * (x_desejado - x[j]) / (x[i] - x[j])

        resultado = resultado + termo

    return resultado

# ===== Primeiro grau =====
x1 = np.array([3.0, 4.0])
y1 = np.array([7.0, 3.0])

f1 = lagrange(x1, y1, x_desejado)

# ===== Segundo grau =====
x2 = np.array([2.5, 3.0, 4.0])
y2 = np.array([6.5, 7.0, 3.0])

f2 = lagrange(x2, y2, x_desejado)

# ===== Terceiro grau =====
x3 = np.array([2.0, 2.5, 3.0, 4.0])
y3 = np.array([5.0, 6.5, 7.0, 3.0])

f3 = lagrange(x3, y3, x_desejado)

# ===== Resultados =====
print("Lagrange 1º grau:")
print("f(3.4) =", f1)

print("\nLagrange 2º grau:")
print("f(3.4) =", f2)

print("\nLagrange 3º grau:")
print("f(3.4) =", f3)

# ===== Gráfico =====
x_plot = np.linspace(2.0, 4.2, 200)

y_plot1 = np.zeros(len(x_plot))
y_plot2 = np.zeros(len(x_plot))
y_plot3 = np.zeros(len(x_plot))

for i in range(len(x_plot)):
    y_plot1[i] = lagrange(x1, y1, x_plot[i])
    y_plot2[i] = lagrange(x2, y2, x_plot[i])
    y_plot3[i] = lagrange(x3, y3, x_plot[i])

plt.figure(figsize=(8, 5))

# Dados originais
plt.plot(df['x'], df['y'], 'or', label='Dados da Tabela')

# Polinômios de Lagrange
plt.plot(x_plot, y_plot1, '-k', label='Lagrange 1º Grau')
plt.plot(x_plot, y_plot2, '-b', label='Lagrange 2º Grau')
plt.plot(x_plot, y_plot3, '-g', label='Lagrange 3º Grau')

# Pontos estimados em x = 3.4
plt.plot(x_desejado, f1, 'ok', label='f(3.4) 1º Grau')
plt.plot(x_desejado, f2, 'ob', label='f(3.4) 2º Grau')
plt.plot(x_desejado, f3, 'og', label='f(3.4) 3º Grau')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Questão 4b - Interpolação de Lagrange')
plt.legend()
plt.grid(True)
plt.show()