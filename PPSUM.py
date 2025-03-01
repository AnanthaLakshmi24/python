# cook your dish here
t  = int(input())
for i in range(t):
    D,N  = map(int,input().split())
    count = 1
    for i in range(1,D+1):
        count = N*(N+1)//2
        N = count
    print(count)
