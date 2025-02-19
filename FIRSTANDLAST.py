# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    maxi=0
    for i in range(n):
        if i < ( n - 1):
            maxi = max(maxi, l[i] + l[i+1])
        else:  
            maxi = max(maxi, l[i] + l[0])  
    print(maxi)
        
        