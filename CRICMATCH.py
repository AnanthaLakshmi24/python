# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    max_runs=6*6*m 
    if max_runs>=n:
        print("YES")
    else:
        print("NO")