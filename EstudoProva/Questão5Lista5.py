import numpy as np
import matplotlib.pyplot as plt

# Dados
x = np.array([0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.5, 1.8])
y = np.array([0.75, 1.25, 1.45, 1.25, 0.55, 0.35, 0.28, 0.18])

# Linearização
Y = np.log(y/x)

# Ajuste linear
beta, ln_alpha = np.polyfit(x, Y, 1)

# Voltando ao modelo original
alpha = np.exp(ln_alpha)

# Valores ajustados
y_ajustado = alpha * x * np.exp(beta*x)

# Resultados
print(f"alpha = {alpha:.4f}")
print(f"beta = {beta:.4f}")
print(f"Modelo: y = {alpha:.4f} * x * e^({beta:.4f}x)")

# Gráfico
plt.scatter(x, y, label="Dados")
plt.plot(x, y_ajustado, label="Ajuste")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()