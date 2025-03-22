# cook your dish here
t=int(input())
for _ in range(t):
    n,k = map(int,input().split())
    l=list(map(int,input().split()))
    r = 0
    d = 0
    for i in range(len(l)):
        if l[i]+r < k:
            print('NO', i+1)
            break
        else:
            r = (l[i]+r) - k
            d += 1
    if d == len(l):
        print('YES')