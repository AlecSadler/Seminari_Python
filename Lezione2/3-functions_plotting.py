import matplotlib.pyplot as pl
import numpy as np

x=np.arange(20.)
pl.plot(x)           #traccia il grafico

pl.clf()     #cancella il grafico

x2=x**2
x3=x**3
pl.plot(x,x,"b.",x,x2,"rd",x,x3,"g^")  #traccia 3 curve nella stessa figura
pl.show()



