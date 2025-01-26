t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    arr=[]
    for i in range(x):
        max1=max(a)
        arr.append(max1)
        a.remove(max1)
        i-=1
    min1=min(arr)
    print(min1-1)
