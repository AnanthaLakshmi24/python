# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    k=a*100//10
    p=b*100//20
    if k>p:
        print("FIRST")
    elif k==p:
        print("ANY")
    else:
        print("SECOND")