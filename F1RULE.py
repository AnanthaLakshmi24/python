# cook your dish here
t=int(input())
for j in range(t):
    x,y=map(int,input().split())
    z=1.07*x 
    if y<=z:
        print("YES")
    else:
        print("NO")