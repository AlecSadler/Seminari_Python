import numpy as np
import matplotlib.pyplot as pl
import os

curdir=os.getcwd()   #prende il path della cartella corrente
fdr='%s/data'%(curdir)
os.chdir(fdr)   #cambia directory

fig=pl.figure(1,figsize=(20,10))   #crea figura

ax=fig.add_subplot(111)
i=0

for f in sorted(os.listdir(fdr)):
    x=np.loadtxt(f)   #estrae i dati dalla cartella
    ax.plot(x[:,1],x[:,0],lw=4)  #plot HR diagram
    i=i+1

fig.gca().invert_xaxis() #inverte l'asse x

ax.set_xlabel("Tempratura Efficace")
ax.set_ylabel("Luminosità")

pl.show()




