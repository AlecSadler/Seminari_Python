#Create a tuple with 10 ages. Print the number of persons with ages larger than 20.

ages= (23,41,18,2,14,27)
print("Tuple: ",ages)
count=int(0)
for i in range (0,len(ages),1):
    if ages[i]>20:
        count=count+1
print("Ages larger than 20: ",count)


