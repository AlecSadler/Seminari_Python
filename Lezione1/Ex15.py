#Plotting two functions

import numpy as np
import matplotlib.pyplot as pl

def f(x):
    a=float(2.0)
    xo=float(10.0)
    c=float(5.0)
    y= (a*c)**(-((x-xo)**2)/2*(c**2))
    return y

def g(x):
    b=float(5.0)
    xo=float(10.0)
    y=b/( ( (x-xo)**2 ) + b*+2)
    return y

if __name__ == "__main__":
    x=np.arange(-50.,50.)
    p1=pl.plot(x,f(x),"c")
    p2=pl.plot(x,g(x),"m")
    pl.xlabel("X AXIS")
    pl.ylabel("Y AXIS")
    pl.text(13,0.8,"f(x)",color="c",fontweight="bold",fontsize=14)
    pl.text(-4.8,0.15,"g(x)",color="magenta",fontweight="bold",fontsize=14)
    pl.show()


