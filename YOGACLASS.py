# cook your dish here
for i in range(int(input())):
    n,x,y=map(int,input().split())
    onehr=n*x
    if n%2==0:
        twohr=(n//2)*y 
    else:
        twohr=(n//2)*y + x
    
    print(max(onehr,twohr))