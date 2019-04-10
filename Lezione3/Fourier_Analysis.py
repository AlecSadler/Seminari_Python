import matplotlib.pyplot as pl
import numpy as np
from scipy.fftpack import fft, fftfreq

#serie fourier

def fun(t,f):
    return np.sin(2*np.pi*f*t)-1/2*np.sin(2*np.pi*2*f*t)-1/2*np.sin(2*np.pi*f/4*t)

f=400.
ns=16
T=1/f
dt=T/ns

t=np.linspace(0, dt * (ns * 4 - 1), ns * 4)
pl.plot(t,fun(t,f),'k-')
pl.plot(t,fun(t,f),'ro')
pl.show()
ln=len(t)
y1=fft(fun(t,f)/ln)
f1=fftfreq(ln,dt)
pl.figure()
i=f1>=0
pl.vlines(f1[i],0,np.abs(y1[i]))
pl.ylim(0,0.5)
pl.xlabel('Frequency (Hz)')
pl.ylabel('Amplitude')
       
t=np.linspace(0,dt*(ns*3.25-1),int(ns*3.25))
pl.figure()
pl.plot(t,fun(t,f),'k-')
pl.plot(t,fun(t,f),'ro')
ln=len(t)
y2=fft(fun(t,f)/ln)
f2=fftfreq(ln,dt)
pl.figure()
i=f2>=0
pl.vlines(f2[i],0,np.abs(y2[i]))
pl.ylim(0,0.5)
pl.xlabel('Frequency (Hz)')
pl.ylabel('Amplitude')

y=np.pad(fun(t,f),(0,max([0,64-len(t)])),mode='constant',constant_values=0)
ln=len(t)
y3=fft(fun(t,f)/ln)
f3=fftfreq(ln,dt)
pl.figure()
i=f3>=0
pl.vlines(f3[i],0,np.abs(y3[i]))
pl.ylim(0,0.5)
pl.xlabel('Frequency (Hz)')
pl.ylabel('Amplitude')

pl.show()
