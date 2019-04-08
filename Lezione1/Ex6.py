#Print a random number between 1 and 20 and calculate if that number has 1 or 2 digits.

import random

n=random.randint(1,20)
print("Numero Randomizzato: ",n)
n_str=str(n)
print("Numero cifre di n: ",len(n_str))




