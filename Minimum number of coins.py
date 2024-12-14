t = int(input())
for i in range(t):
    x = int(input())
    
    if x % 5 != 0:
        print(-1)
    elif x % 10 == 0:
        print(x // 10)
    else:
        print(x // 10 + 1)