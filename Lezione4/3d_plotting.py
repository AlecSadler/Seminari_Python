import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)


z=x**2+y**4


fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_surface(x, y, z, color='red')

plt.show()





