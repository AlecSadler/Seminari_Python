import numpy as np
import matplotlib.pyplot as pl
import scipy.integrate as intg

def fun1(x):
    return np.exp(-(x**2))

def fun2(a,p,s,x):
    return a*np.exp(-(p-x)**2/s**2)

a=1.5
p=1
s=1.5

x=np.linspace(-3,50,100)
pl.plot(x,fun1(x),'-r')
pl.plot(x,fun2(a,p,s,x),'-b')

i1=intg.quad(fun1,-np.inf,np.inf)
i2=intg.quad(fun2,-2,5,args=(a,p,s))

pl.show()


