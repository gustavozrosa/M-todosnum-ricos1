import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return np.sin(10*x) + np.cos(3*x)

# Vetor x
x= np.linspace(3,6,100) 

# Figura
plt.figure()    
plt.plot(x, f(x), '-b',label='$f(x) = sin(10x)+cos(3x)$')
plt.ylabel("$f(x)$")
plt.xlabel("$x$")
plt.legend()
plt.grid()

plt.show()
