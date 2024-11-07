import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 10000)
y = (np.cos(x))**0.5*np.cos(200*x)+(abs(x))**0.5-np.pi/4*(4-x**2)**0.01
plt.plot(x, y, color='#db44a1', linewidth=15)
plt.axhline(0, color = 'black')
plt.axvline(0, color = 'black')
plt.show()