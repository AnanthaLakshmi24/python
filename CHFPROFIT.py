# cook your dish here
t=eval(input())
while(t>0):
    x,y,z=map(eval,input().split())
    print((z*x)-(y*x))
    t-=1
