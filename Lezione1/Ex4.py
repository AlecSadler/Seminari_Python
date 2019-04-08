#Shows all numbers power of two less than 10000 as in this way:
'''0001
   0002
   0004
   ....
   8192'''

res=int(1)
str_res=str(res)
print("0"*(4-len(str_res))+str(res))
while (res*2) <= 10000:
    res=res*2
    str_res = str(res)
    print("0"*(4-len(str_res))+str(res))







