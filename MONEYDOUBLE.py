t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    for _ in range(y):
        x = max(x + 1000, 2 * x)
    print(x)