# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    scores = list(map(int, input().split()))
    total = 0
    flag = False
    for i in range(n):
        total += scores[i]
        avg = total / (i + 1)
        if avg < 40:
            print("No")
            flag = True
            break
    if not flag:
        print("Yes")

