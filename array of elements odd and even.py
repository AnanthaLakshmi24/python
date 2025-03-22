n=int(input())
l=list(map(int,input().split()))
even=[]
odd=[]
for i in range(len(l)):
    if l[i]%2==0:
        even.append(l[i])
    else:
        odd.append(l[i])
a=odd+even
print(*a)