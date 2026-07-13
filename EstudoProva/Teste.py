import numpy as np
import matplotlib.pyplot as plt
x = np.array([])
y = np.array([])
a1, a0 = np.polyfit(x, y, 1)
y_ajustado = a0 + a1 * x