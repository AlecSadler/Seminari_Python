import numpy as np
import matplotlib.pyplot as pl
from scipy.integrate import odeint


#definisce una funzione e calcola la derivata
def dy_dx(y,x):
    return x-y

xs= np.linspace(0,5,100)
yo= 1.0      #calcola la condizione iniziale
ys= odeint(dy_dx,yo,xs)
pl.plot(ys)
pl.plot(xs-1+2*np.exp(-xs),'dr')

pl.show()
