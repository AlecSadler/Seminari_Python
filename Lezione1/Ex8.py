#Create a random number between 1 and 1000. Print a message showing the number of digits.

import random

n=random.randint(1,1000)
print(n)
str_n=str(n)
print("The random number has",len(str_n),"digits.")



