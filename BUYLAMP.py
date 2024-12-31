# Input reading
T = int(input())
for _ in range(T):
    N, K, X, Y = map(int, input().split())
    if K == 0:
        cost = N * min(X, Y)
    elif X <= Y:
        cost = N * X
    else:
        cost = K * X + (N - K) * Y
    print(cost)