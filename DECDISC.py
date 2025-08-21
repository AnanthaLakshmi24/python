t = int(input())
for _ in range(t):
    n= int(input())
    prices = list(map(int, input().split()))
    min_total_cost = float('inf')

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if j == i + 1:
                cost = prices[i] + prices[j] // 2
            else:
                cost = prices[i] + prices[j]
            min_total_cost = min(min_total_cost, cost)

    print(min_total_cost)
