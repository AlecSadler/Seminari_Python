#Create 3 random numbers between 1 and 100. Shows a message if all of them are higher than 10.

import random

n1=random.randint(1,100)
n2=random.randint(1,100)
n3=random.randint(1,100)
print(n1,n2,n3)
if n1>10 and n2>10 and n3>10:
    print("All numbers are higher than 10.")



