#Find and show the sum of all multiples of 3 or 5 less than 1000 (this number is 233168)

sum=int(0)
n=0
while n<1000:
        if n%3==0 or n%5==0:
            sum=sum+n
        n=n+1
print(sum)





