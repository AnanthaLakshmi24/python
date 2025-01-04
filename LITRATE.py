t=int(input())
for i in range(t):
    p,l=map(int,input().split())
    k=(l*100/p)
    if k>=75:
        print("YES")
    else:
        print("NO")