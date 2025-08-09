# cook your dish here
S = int(input())
for _ in range(S):
    A,T,H = map(int,input().split())
    W = list(map(int,input().split()))
    count = 0
    for weight in W:
        if T <= weight <= H:
            count += 1
    print(count)