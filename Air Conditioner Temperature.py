# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if max(a, c) <= b:
        print("Yes")
    else:
        print("No")