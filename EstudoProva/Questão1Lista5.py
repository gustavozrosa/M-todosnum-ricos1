import numpy as np
import matplotlib.pyplot as plt
x = np.array([2, 4, 6, 7, 10, 11, 14, 17, 20])
y = np.array([4, 5, 6, 8, 8, 10, 12, 17,20])
a1, a0 = np.polyfit(x, y, 1)
y_ajustado = a0 + a1 * x
print(f"Eq da reta ajusta y = {a0: .4f} + {a1: .4f}x")
plt.scatter(x, y, label="dados")
plt.plot(x, y_ajustado, label="reta ajustada")
plt.legend()
plt.show()