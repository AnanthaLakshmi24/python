# cook your dish here
t=int(input())
for i in range(t):
    d,x,y,z=map(int,input().split())
    k=7*x 
    s=(y*d)+(z*(7-d))
    print(max(k,s))