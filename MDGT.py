# cook your dish here
for i in range(int(input())):
    N = int(input())
    H= list(map(int,input().split()))
    
    k= H[-1]
    t = 0
    for i in range(N-1,0,-1):
        if max(H[:i]) >= k:
            t += 1       
    print(t)