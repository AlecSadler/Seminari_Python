import numpy as np
import matplotlib.pyplot as pl
from scipy.integrate import odeint


#calcola le derivate dell'array y
def solve(y,t):
    return [y[1],-2*y[0]-y[1]]

t=np.arange(0,25.0,0.01)
y=odeint(solve,[1,0],t)

pl.plot(t,y[0:,0])
pl.show()