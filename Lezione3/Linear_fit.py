import matplotlib.pyplot as pl
import numpy as np

x=np.linspace(-3,20,100) #spaziatura lineare dati
x=np.random.normal(loc=x,scale=0.25,size=len(x)) #aggiungi qualche errore
y=1.2*x**2-0.3*x+2.8
y=np.random.normal(loc=y,scale=1.5,size=len(y)) #aggiungi errori

pl.plot(x,y,'or')

pl.show()

cc=np.polyfit(x,y,deg=2) #misura polinomio secondo grado

xx=np.linspace(-3,21) #crea x-data per tracciare la misura
yy=np.polyval(cc,xx)   #calcola valori utilizzando cc
pl.plot(xx,yy,'-b')
cc,cov= np.polyfit(x,y,deg=2,cov=True)  #matrice convarianza
np.sqrt(cov.diagonal())

pl.show()
