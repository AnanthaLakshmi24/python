# cook your dish here
t = int(input())
for _ in range(t):
    P = int(input())
    total_solved = (P // 100) + (P % 100)
    if total_solved > 10:
        print(-1)
    else:
        print(total_solved)