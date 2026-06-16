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

# ===== Regressão polinomial =====
coef_grau2 = np.polyfit(df['x'], df['y'], 2)
coef_grau3 = np.polyfit(df['x'], df['y'], 3)

y_grau2 = np.polyval(coef_grau2, df['x'])
y_grau3 = np.polyval(coef_grau3, df['x'])

print("Coeficientes da parábola:")
print(coef_grau2)

print("\nCoeficientes da cúbica:")
print(coef_grau3)

# ===== Cálculos adicionais =====
n = len(df['x'])
y_mean = np.mean(df['y'])
St = np.sum((df['y'] - y_mean)**2)

Sr_grau2 = np.sum((df['y'] - y_grau2)**2)
R2_grau2 = (St - Sr_grau2) / St
Syx_grau2 = math.sqrt(Sr_grau2 / (n - 3))

Sr_grau3 = np.sum((df['y'] - y_grau3)**2)
R2_grau3 = (St - Sr_grau3) / St
Syx_grau3 = math.sqrt(Sr_grau3 / (n - 4))

print("\nParábola:")
print("Sr =", Sr_grau2)
print("R² =", R2_grau2)
print("Erro padrão =", Syx_grau2)

print("\nCúbica:")
print("Sr =", Sr_grau3)
print("R² =", R2_grau3)
print("Erro padrão =", Syx_grau3)

# ===== Gráfico =====
x_plot = np.linspace(min(df['x']), max(df['x']), 100)

y_plot_grau2 = np.polyval(coef_grau2, x_plot)
y_plot_grau3 = np.polyval(coef_grau3, x_plot)

plt.plot(df['x'], df['y'], 'or', label='Dados Discretos')
plt.plot(x_plot, y_plot_grau2, '-b', label='Parábola')
plt.plot(x_plot, y_plot_grau3, '-g', label='Cúbica')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()