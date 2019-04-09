import numpy as np

with open("dio.txt","w") as file:
    for i in np.arange(100.):
        file.write("%d %10.4e\n" % (i,np.exp(i)))

reader= open("dio.txt","r")
dat=[]
for ln in reader:
    t=ln.split()
    dat.append(t)
reader.close()
np.shape(dat)
print(dat)
print(len(dat))

dat=np.array(dat).astype(float)  #converte in array la lista
print(dat)

reader2= open("data2","w")    #legge l'array e crea un file con il suo contenuto
x=np.arange(100.)
y=np.exp(x)
np.savetxt("data2.txt",(x,y))
x,y= np.loadtxt("data2.txt")

k=np.sqrt(np.arange(30)*5)     #salvare contenuto variabile in binario
np.save("mybin.npy",k)
v=np.load("mybin.npy")

