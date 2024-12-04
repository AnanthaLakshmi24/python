# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    k=y*100//x 
    if k>=50:
        print("YES")
    else:
        print("NO")