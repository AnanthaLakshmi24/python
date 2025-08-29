# cook your dish here
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    d = a
    while d*2 > b:
        d-= 1
    print(d + (2*d))