import numpy as np
import matplotlib.pyplot as plt
t = np.array([0, 4, 8, 12, 16, 20])
c = np.array([1600, 1320, 1000, 890, 650, 560])
Y = np.log(c)
b, ln_a = np.polyfit(t, Y, 1)
a = np.exp(ln_a)
c_ajustado = a * np.exp(b*t)
c0 = a
t_200 = np.log(200/a) / b
print(f"Modelo: c = {a:.4f} * e^({b:.4f}t)")
print(f"Concentração em t = 0: {c0:.4f} UFC/100 mL")
print(f"Tempo para c = 200: {t_200:.4f} h")
plt.scatter(t, c, label="Dados")
plt.plot(t, c_ajustado, label="Ajuste exponencial")
plt.xlabel("Tempo (h)")
plt.ylabel("Concentração (UFC/100 mL)")
plt.legend()
plt.grid()
plt.show()