# cook your dish here
def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    if n == 0:
        print(0)
        return
    
    p=[0] * n
    for i in range(n):
        p[i] = arr[i] % 2
    
    length = 1
    for i in range(1,n):
        if p[i] != p[i-1]:
            length +=1
            
    print(length)

t = int(input())
for _ in range(t):
    solve()
