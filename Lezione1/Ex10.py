#Create a random number between 100 and 200. Shows all numbers between 1 and the random number.

import random

n=random.randint(100,200)
print("Random number: ",n)
for i in range(2,n,1):
    print(i)



