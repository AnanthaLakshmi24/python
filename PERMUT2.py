# cook your dish here
while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int,input().split(" ",-1)))
    b = a[:]
    for i in range(n):
        b[a[i] - 1]= i+1

    if b == a:
        print('ambiguous')
    else:
        print('not ambiguous')