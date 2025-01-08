t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    if 2 * max(x, y, z) <= x + y + z + 1:
        print("YES")
    else:
        print("NO")