# cook your dish here
t=int(input())
for i in range(t):
    li=list(map(int,input().split()))
    li.sort()
    print(li[-2])