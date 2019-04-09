import matplotlib.pyplot as plt
import numpy as np
import math
import random

sine=np.sin(np.arange(1,100))
cosx=np.cos(np.arange(1,100))
cubic=(np.arange(-10,10))**3
lgr=np.log(np.arange(1,100))

fun=[sine,cosx,cubic,lgr]


#GENERA LA FIGURA CON LE DIMENSIONI
fig=plt.figure(1,figsize=(9,6))

#CREO DUE LISTE CON I TITOLI DEI GRAFICI E I COLORI DEGLI ISTOGRAMMI
labels=['Sine','Cosine','Tangent','Logarithmic']
colors=['red','blue','orange','black']

Naxis=221  #DISPOSIZIONE DEI GRAFICI 2 RIGHE- 2 COLONNE 1=PASSO INDICE

#ITERAZIONE CHE CREA I 6 ISTOGRAMMI PRENDENDO I PARAMETRI DALLE LISTE CREATE
for i in range(0,4):
    ax=fig.add_subplot(Naxis)
    p=ax.plot(fun[i],color=colors[i])
    ax.set_title(labels[i])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    Naxis=Naxis+1

plt.suptitle('ELEMENTARY FUNCTIONS')

#AGGIUSTA GLI SPAZI TRA I PLOT
fig.subplots_adjust(wspace=0.5,hspace=0.8)

plt.show()

