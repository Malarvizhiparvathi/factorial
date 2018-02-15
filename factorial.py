num=7
fact=1
if (num<0):
    print("fact does not exist for negative numbers")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
