import numpy as np
import matplotlib.pyplot as plt
T_celsius = np.array([-40, 0, 40, 80, 120, 160])
p = np.array([6900, 8100, 9350, 10500, 11700, 12800])
T = T_celsius + 273.15
V = 10      # m³
n = 1      # kg
a = np.sum(T*p) / np.sum(T**2)
R = a * V / n
p_ajustado = a*T
print(f"Coeficiente angular = {a:.4f}")
print(f"Constante R = {R:.4f}")
plt.scatter(T, p, label="Dados")
plt.plot(T, p_ajustado, label="Ajuste")
plt.xlabel("Temperatura (K)")
plt.ylabel("Pressão (N/m²)")
plt.legend()
plt.grid()
plt.show()