'''Write a function to read a list of numbers giving as a result the cumulative sum, i.e. a list where each element
i of the list is the sum of the n first elements of the original list.'''

def sum_list (l):
    sum=int(0)
    for i in range (0,len(l),1):
        sum=sum + l[i]
    return sum

def build_sumlist (l):
    sumliist=[0]
    el=int(0)
    for i in range (1,len(l)+1,1):
        el=el+l[i-1]
        sumliist.append(el)
    return sumliist




if __name__ == "__main__":
    l1=[3,7,9,23,1,4]
    print("Somma di tutti gli eementi: ",sum_list(l1))
    print("Lista in cui ogni elemento è somma dei precedenti: ",build_sumlist(l1))






