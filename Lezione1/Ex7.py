'''Asign to a variable an integer number between 1 and 100. In a loop, create a random number also between 1
and 100. Stop the loop if the random number matchs the value of the first variable and show a message.'''

import random

n1=random.randint(1,100)
n2=int
found=False
while found==False:
    n2=random.randint(1,100)
    if n2==n1:
        found=True
        print("Trovato!","n1=",n1,"n2=",n2)




