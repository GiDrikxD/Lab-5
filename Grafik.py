import numpy as np
import matplotlib.pyplot as plt

N = 23
x = np.linspace(0, 1, 1000) 
y = np.sin(np.pi * x / N)     

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графік функції f(x) = sin(pi*x/N) для N = 23')
plt.grid(True)
plt.show()
