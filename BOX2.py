# cook your dish here
t=int(input())
for _ in range(t):
    a,b,k=map(int,input().split())
    s=abs(a-b)
    if s==k:
        print("0")
        continue
    if (a+b-k) % 2 != 0:
        print("-1")
        continue
    else:
        print(abs(s-k) // 2)