#Write a function which takes three integers and shows the sum of only the two higher ones.

def sum_highers(a,b,c):
    if a>b:
        if c>b:
            return a+c
        else:
            return a+b
    else:
        if a>c:
            return a+b
        else:
            return b+c

if __name__ == "__main__":
    a=int(input())
    b=int(input())
    c=int(input())
    print(sum_highers(a,b,c))
