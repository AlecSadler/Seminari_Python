import matplotlib.pyplot as plt
import numpy as np

Nsam=10000 #LIMITE MASSIMO RANDOMIZZAZIONE X
Nbin=100   #NUMERO RETTANGOLI DELL'ISTOGRAMMA

#GENERO LE VARIE DISTRIBUZIONI DEI DATI
x0=np.random.uniform(0,1,Nsam)
x1=np.random.normal(0,1,Nsam)
x2=np.random.triangular(0,3,5,Nsam)
x3=np.random.exponential(2,Nsam)
x4=np.random.chisquare(20,Nsam)
x5=np.random.power(3,Nsam)

#LISTA DELLE CURVE SU CUI ITERARE PER GENERARE LA FIGURA
lst=[x0,x1,x2,x3,x4,x5]

#GENERA LA FIGURA CON LE DIMENSIONI
fig=plt.figure(1,figsize=(9,6))

#CREO DUE LISTE CON I TITOLI DEI GRAFICI E I COLORI DEGLI ISTOGRAMMI
labels=['Uniform','Normal','Triangular','Exponential','Chisquare','Power']
colors=['red','blue','orange','black','green','purple']

Naxis=321

#ITERAZIONE CHE CREA I 6 ISTOGRAMMI PRENDENDO I PARAMETRI DALLE LISTE CREATE
for i in range(0,6):
    ax=fig.add_subplot(Naxis)
    n,b,p=ax.hist(lst[i],bins=Nbin,color=colors[i],range=(lst[i].min(),lst[i].max()))
    ax.set_title(labels[i])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    Naxis=Naxis+1

plt.suptitle('RANDOM & SUBPLOTS')
#AGGIUSTA GLI SPAZI TRA I PLOT
fig.subplots_adjust(wspace=0.5,hspace=0.8)

plt.show()

