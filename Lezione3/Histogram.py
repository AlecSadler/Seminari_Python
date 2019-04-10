import matplotlib.pylab as pl
import numpy as np
import math as mt

mu=5
s=np.random.poisson(mu,10000)

count,bins,ignored=pl.hist(s,10,density=True)

bin=np.arange(max(s))
n=[]
for i in bin:
    n.append(mt.factorial(i))
pl.plot(bin,mu**bin/n*np.exp(-mu),linewidth=2,color="r")
pl.show()
