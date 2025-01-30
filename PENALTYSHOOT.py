# cook your dish here
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a + 2 >= b and b + 1 >= a:
        print("YES")
    else:
        print("NO")
