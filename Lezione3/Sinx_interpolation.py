import matplotlib.pyplot as pl
import numpy as np

x=np.linspace(0,2*np.pi,10)
y=np.sin(x)
xvals= np.linspace(0,2*np.pi,50)
yinterp=np.interp(xvals,x,y)
pl.plot(x,y,'o')
pl.plot(xvals,yinterp,'-x')
pl.show()