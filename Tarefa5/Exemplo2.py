# ===== Bibliotecas =====
import numpy as np
import math 
import pandas as pd
import matplotlib.pyplot as plt

# ===== Dados de entrada =====
date = {
    'x': [1, 2, 3, 5, 10, 20, 30, 40, 50],
    'y': [0.07, 0.13, 0.22, 0.275, 0.4, 0.6, 0.7, 0.75, 0.78]
}

df = pd.DataFrame(date)

plt.figure()
plt.plot(df['x'], df['y'], 'or', label='Dados Discretos')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
# ===== Linearização dos dados =====

df['x'] = 1/(df['x'])
df['y'] = 1/(df['y'])

# ===== Cálculos =====
n = len(df['x'])
sum_x = np.sum(df['x'])
sum_y = np.sum(df['y'])
sum_xx = np.sum(df['x']**2)
sum_yx = np.sum(df['y']*df['x'])

# ===== Construindo as Matrizes A e b =====
A = np.array([[n, sum_x], [sum_x, sum_xx]])
b = np.array([sum_y, sum_yx])

# ===== Solução do Sistema Linear =====
ai = np.linalg.solve(A,b)

# ===== Gráfico =====
plt.figure()
plt.plot(df['x'], df['y'], 'or', label='Dados Discretos')
plt.plot(df['x'], ai[0]+ai[1]*df['x'], '-b', label='Ajuste Linear')
plt.legend()
plt.xlabel('1/x')
plt.ylabel('1/y')
plt.show()

# ===== Cálculos Adicionais =====
Sr = np.sum((df['y'] - ai[0] - ai[1]*df['x'])**2)

y_mean = np.mean(df['y'])
St = np.sum((df['y'] - y_mean)**2)

R2 = ((St - Sr)/St)
print(R2)