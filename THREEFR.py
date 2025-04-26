# cook your dish here
t = int(input())
for _ in range(t):
    A = sorted(list(map(int, input().split())))
    if sum(A[0:2]) == A[2]:
        print("yes")
    else:
        print("no")