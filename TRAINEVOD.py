# cook your dish here
t = int(input())
for _ in range(t):
    x = int(input())
    l = list(map(int,input().split()))
    even=0
    odd=0
    for i in range(len(l)):
        if i%2==0:
            even=even+l[i]
        else:
            odd=odd+l[i]
    if even>=odd:
        print(even)
    else:
        print(odd)