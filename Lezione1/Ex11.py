'''Create a function which takes an integer and prints the multiples of that number (for example, if takes 3 it must
show all the multiples up to 30)'''

def multiples(n):
    for i in range (0,11,1):
        print(n*i)
    return None

if __name__ == "__main__":
    n=int(input("Insert number: "))
    multiples(n)


