# cook your dish here

for t in range(int(input())):

    n,x = map(int,input().split())
    N = list(map(int,input().split()))
    m = 0
    for i in range(n):
        if(N[i]<x):
            m=i+1 
    print(m)
