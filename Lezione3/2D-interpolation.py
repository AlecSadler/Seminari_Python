import matplotlib.pyplot as pl
import numpy as np
from scipy.interpolate import interp2d as int2d


x=np.arange(-5.01,5.01,0.25)
y=np.arange(-5.01,5.01,0.25)
xx,yy=np.meshgrid(x,y)
z=np.sin(xx**2+yy**2)
f=int2d(x,y,z,kind='cubic')


xnew=np.arange(-5.01,5.01,1e-2)
ynew=np.arange(-5.01,5.01,1e-2)
znew=f(xnew,ynew)
pl.figure()
pl.pcolormesh(xx,yy,z)
pl.figure()
pl.pcolormesh(xnew,ynew,znew)

int2d(x,y,z,kind='linear',copy=True,bounds_error=False,fill_value=np.nan)
pl.show()