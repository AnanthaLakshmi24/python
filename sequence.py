t=int(input())
print(t,end=" ")
while(t!=0):
    if t%2==0:
        t=t//2
        if (t==1):
            break
        print(t,end=" ")
    else:
        t=3*t+1
        if (t==1):
            break
        print(t,end=" ")
    
