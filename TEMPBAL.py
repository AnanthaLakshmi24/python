t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total_seconds = 0
    current_balance = 0
    for i in range(n):
        current_balance += a[i]
        total_seconds += abs(current_balance)
    print(total_seconds)