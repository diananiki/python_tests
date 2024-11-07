import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5*np.pi, 5*np.pi, 400)
plt.plot(x, np.cos(x+np.pi/7), color='red')
plt.plot(x, np.cos(x+2*np.pi/7), color='orange')
plt.plot(x, np.cos(x+3*np.pi/7), color='yellow')
plt.plot(x, np.cos(x+4*np.pi/7), color='green')
plt.plot(x, np.cos(x+5*np.pi/7), color='skyblue')
plt.plot(x, np.cos(x+6*np.pi/7), color='blue')
plt.plot(x, np.cos(x+np.pi), color='purple')
plt.show()