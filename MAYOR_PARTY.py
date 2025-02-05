# cook your dish here
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    print(max(a+c,b))