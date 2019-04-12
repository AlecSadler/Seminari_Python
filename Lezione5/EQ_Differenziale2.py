import numpy as np
import matplotlib.pyplot as pl
from scipy.integrate import odeint


#calcola le derivate dell'array y
def dydt(y,t):
    a= -2.0
    b= -0.1
    return [y[1],a*y[0]+b*y[1]]

time= np.linspace(0.0,10.0,1000)
yinit= [0.0005,0.2]        #condizione iniziale
y= odeint(dydt,yinit,time)
pl.figure()
pl.plot(time,y[:,0])
pl.xlabel('t')
pl.ylabel('y')

pl.show()
