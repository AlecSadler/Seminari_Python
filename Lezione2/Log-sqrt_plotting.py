import matplotlib.pyplot as pl
import numpy as np

xx = np.arange(50)
yy = np.sqrt(xx)

fig = pl.figure()
ax = fig.add_axes ([0.15,0.15,0.8,0.8])

#COSTRUISCO IL GRAFICO DA 0
ax.tick_params(axis="x",labelsize=18)
ax.tick_params(axis="y",labelsize=18)
ax.minorticks_on()
ax.tick_params("both",length=10,width=2,which="major")
ax.tick_params("both",length=5,width=1,which="minor")
ax.get_yaxis().set_tick_params(direction="in",which="both")
ax.get_xaxis().set_tick_params(direction="in",which="both")

#LEGENDA
ax.plot(xx,yy,"-k",lw=2,label="Sqrt")
ax.plot(xx,np.log10(xx),".r",label="Log10")

#RANGE ASSI
ax.set_xlim([-1,100])
ax.set_ylim([0,15])

#NOMI ASSI
ax.set_xlabel("x-data",fontsize=18)
ax.set_ylabel("y-data",fontsize=18)

pl.legend()
pl.show()

#SALVA LA FIGURA SU FILE
fig.savefig("myplot.eps")




