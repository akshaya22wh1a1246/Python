lb=int(input("ENter lb:"))
ub=int(input("Enter ub:"))
for n in range(lb,ub+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)
