# cook your dish here
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    req = 50 - a
    min_sum = 2 * b
    max_sum = 2 * b + 10
    if min_sum <= req <= max_sum:
        print("yes")
    else:
        print("no")