# cook your dish here
t = int(input())
for _ in range(t):
    p, q = map(int, input().split())
    total_serves = p + q
    turns = total_serves // 2
    if turns % 2 == 0:
        print("Alice")
    else:
        print("Bob")
