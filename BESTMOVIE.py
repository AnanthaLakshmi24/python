# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    min_cost = float('inf')
    for _ in range(n):
        a,b = map(int, input().split())
        if a >= 7:
            min_cost = min(min_cost, b)
    if min_cost == float('inf'):
        print(-1)
    else:
        print(min_cost)