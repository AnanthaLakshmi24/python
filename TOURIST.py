# cook your dish here
T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    min_distance = float('inf')  # Start with a large number
    for _ in range(N):
        X, Y = map(int, input().split())
        distance = abs(A - X) + abs(B - Y)
        min_distance = min(min_distance, distance)
    print(min_distance)
