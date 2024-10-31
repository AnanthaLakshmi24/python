# cook your dish here
t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    if n>=s:
        print(s)
    elif n<s:
        print (abs(2*n-s))