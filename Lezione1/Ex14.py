#Create a list with 10 ages. Erase all the ages smaller than 18.

ages= [23,41,18,2,14,27]
print("List: ",ages)
adults=list()
for i in range(0,len(ages),1):
    if ages[i]>=18:
        adults.append(ages[i])
print("Ages larger than 18: ",adults)


