# cook your dish here
for _ in range(int(input())):
    a=list(map(int,input().split()))
    a1=a[:6//2]
    a1.sort(reverse=True)
    a2=a[6//2:]
    a2.sort(reverse=True)
    a3=max((a1,a2))
    if a1==a2:
        print("Tie")
    elif a3==a1:
        print("Alice")
    elif a3==a2:
        print("Bob")
