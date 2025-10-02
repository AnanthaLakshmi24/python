# cook your dish here
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort(reverse=True)
    print(sum(l[:k]))