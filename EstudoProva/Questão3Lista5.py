import numpy as np
import matplotlib.pyplot as plt

# Dados
v = np.array([10, 20, 30, 40, 50, 60, 70, 80])
Ft = np.array([25, 70, 380, 550, 610, 1220, 830, 1450])

# Linearização com ln
x = np.log(v)
y = np.log(Ft)

# Ajuste linear nos dados transformados
b, ln_a = np.polyfit(x, y, 1)

# Voltando para o modelo original
a = np.exp(ln_a)

# Valores ajustados
Ft_ajustado = a * v**b

# Resultados
print("Modelo de potência:")
print(f"Ft = {a:.4f} * v^{b:.4f}")

# Gráfico
plt.scatter(v, Ft, label="Dados")
plt.plot(v, Ft_ajustado, label="Ajuste de potência")
plt.xlabel("v (m/s)")
plt.ylabel("Ft (N)")
plt.legend()
plt.grid()
plt.show()