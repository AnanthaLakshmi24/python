# cook your dish here
t =int(input())
for _ in range(t):
    n,k = map(int,input().split())
    if n==k:
        print('0')
    elif k>(n//2):
        print(n-k)
    else:
        print(k)
        