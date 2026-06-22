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

# ============================================================
# QUESTÃO 1a - REGRESSÃO LINEAR
# ============================================================

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

# ===== Valores ajustados da reta =====
y_ajustado = a0 + a1 * df['x']

# ===== Cálculos Adicionais da reta =====
Sr = np.sum((df['y'] - y_ajustado)**2)

y_mean = np.mean(df['y'])
St = np.sum((df['y'] - y_mean)**2)

R2 = (St - Sr) / St
r = math.sqrt(R2)

Syx = math.sqrt(Sr / (n - 2))

# ===== Resultados da reta =====
print("===== QUESTÃO 1a - REGRESSÃO LINEAR =====")
print("Equação da reta:")
print("y =", a0, "+", a1, "x")
print("Interseção com o eixo y =", a0)
print("Inclinação =", a1)
print("Sr =", Sr)
print("St =", St)
print("R² =", R2)
print("Coeficiente de correlação r =", r)
print("Erro padrão da estimativa Sy/x =", Syx)

# ============================================================
# QUESTÃO 1b - REGRESSÃO POLINOMIAL
# ============================================================

# ===== Regressão polinomial =====
coef_grau2 = np.polyfit(df['x'], df['y'], 2)
coef_grau3 = np.polyfit(df['x'], df['y'], 3)

y_grau2 = np.polyval(coef_grau2, df['x'])
y_grau3 = np.polyval(coef_grau3, df['x'])

# ===== Cálculos adicionais da parábola =====
Sr_grau2 = np.sum((df['y'] - y_grau2)**2)
R2_grau2 = (St - Sr_grau2) / St
Syx_grau2 = math.sqrt(Sr_grau2 / (n - 3))

# ===== Cálculos adicionais da cúbica =====
Sr_grau3 = np.sum((df['y'] - y_grau3)**2)
R2_grau3 = (St - Sr_grau3) / St
Syx_grau3 = math.sqrt(Sr_grau3 / (n - 4))

# ===== Resultados da parábola e da cúbica =====
print("\n===== QUESTÃO 1b - REGRESSÃO POLINOMIAL =====")

print("\nCoeficientes da parábola:")
print(coef_grau2)
print("Equação da parábola:")
print("y =", coef_grau2[0], "x² +", coef_grau2[1], "x +", coef_grau2[2])
print("Sr =", Sr_grau2)
print("R² =", R2_grau2)
print("Erro padrão =", Syx_grau2)

print("\nCoeficientes da cúbica:")
print(coef_grau3)
print("Equação da cúbica:")
print("y =", coef_grau3[0], "x³ +", coef_grau3[1], "x² +", coef_grau3[2], "x +", coef_grau3[3])
print("Sr =", Sr_grau3)
print("R² =", R2_grau3)
print("Erro padrão =", Syx_grau3)

# ============================================================
# GRÁFICO ÚNICO
# ============================================================

x_plot = np.linspace(min(df['x']), max(df['x']), 200)

# reta
y_plot_reta = a0 + a1 * x_plot

# parábola
y_plot_grau2 = np.polyval(coef_grau2, x_plot)

# cúbica
y_plot_grau3 = np.polyval(coef_grau3, x_plot)

plt.figure(figsize=(8, 5))

plt.plot(df['x'], df['y'], 'or', label='Dados Discretos')
plt.plot(x_plot, y_plot_reta, '-k', label='Ajuste Linear')
plt.plot(x_plot, y_plot_grau2, '-b', label='Parábola')
plt.plot(x_plot, y_plot_grau3, '-g', label='Cúbica')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparação dos Ajustes - Linear, Parabólico e Cúbico')
plt.grid(True)

plt.show()