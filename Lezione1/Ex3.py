'''Write a function called ’middle’ which takes a list and give back a new list cotaining all elements
except the first and last.'''

def middle (l):
    middlelist=list()
    l.remove(l[len(l)-1])
    l.remove(l[0])
    middle_list=l
    return middle_list

if __name__ == "__main__":
    l1=[3,7,9,23,1,4]
    print("Lista iniziale: ",l1)
    print("Lista dopo CHOP: ",middle(l1))






