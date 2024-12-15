# cook your dish here
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    k=max(l)
    l.remove(k)
    p=max(l)
    print(p)