# cook your dish here
t=int(input())
for _ in range(t):
    N=int(input())
    odds = (N + 1) // 2
    evens = N // 2
    print(odds * evens * 2)