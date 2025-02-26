# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    c= 0
    # D = list(map(int, input().split())
    d= int(input())
    while d> 0:
        k = d % 10
        if k % 5 == 0:
            c= c+1
        d //= 10
    if c== 0:
        print("No")
    elif c> 0:
        print("Yes")