import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

# ===== Dados de entrada =====
date = {
    'x': [0.00, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50],
    'y': [-8.00, -6.50, -2.30, -0.50, -0.20, 0.05, 0.10, 0.30, 0.40, 0.30, 0.50, 0.26, 0.90, 3.50, 6.50]
}

df = pd.DataFrame(date)

# ===== Cálculos =====
n = len(df['x'])
sum_x = np.sum(df['x'])
sum_y = np.sum(df['y'])
sum_xx = np.sum(df['x']**2)
sum_yx = np.sum(df['y'] * df['x'])

# ===== Construindo as Matrizes A e b =====
A = np.array([[n, sum_x],
              [sum_x, sum_xx]])

b = np.array([sum_y, sum_yx])

# ===== Solução do Sistema Linear =====
ai = np.linalg.solve(A, b)

a0 = ai[0]
a1 = ai[1]

print("Interseção com o eixo y =", a0)
print("Inclinação =", a1)

# ===== Valores ajustados =====
y_ajustado = a0 + a1 * df['x']

# ===== Gráfico =====
plt.plot(df['x'], df['y'], 'or', label='Dados Discretos')
plt.plot(df['x'], y_ajustado, '-b', label='Ajuste Linear')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# ===== Cálculos Adicionais =====
Sr = np.sum((df['y'] - y_ajustado)**2)

y_mean = np.mean(df['y'])
St = np.sum((df['y'] - y_mean)**2)

R2 = (St - Sr) / St
r = math.sqrt(R2)

Syx = math.sqrt(Sr / (n - 2))

print("Sr =", Sr)
print("St =", St)
print("R² =", R2)
print("Coeficiente de correlação r =", r)
print("Erro padrão da estimativa Sy/x =", Syx)