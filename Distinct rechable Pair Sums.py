# cook your dish here
T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    print(2 * R - 2 * L + 1)