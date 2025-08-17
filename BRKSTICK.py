# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    A = list(map(int, input().split()))
    max_breaks = sum(a - 1 for a in A if a > 1)
    print(max_breaks)
