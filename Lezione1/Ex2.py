#Write a function called ’chop’ which takes a list and remove the first and last element, but return nothing.

def chop (l):
    l.remove(l[len(l)-1])
    l.remove(l[0])
    return None

if __name__ == "__main__":
    l1=[3,7,9,23,1,4]
    print("Lista iniziale: ",l1)
    chop(l1)
    print("Lista dopo CHOP: ",l1)






