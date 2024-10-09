# cook your dish here
t=int(input())
for _ in range(t):
    li=list(map(int,input().split()))
    total=sum(li)
    for profit in li:
        if profit>total-profit:
            print("YES")
            break
    else:
        print("NO")