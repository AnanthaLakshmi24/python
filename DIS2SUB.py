# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    lis= list(map(int, input().split()))
    if len(set(lis))==1:
        print(-1)
    else:
        print(2)
        
    