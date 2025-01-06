# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    x=100-a
    y=200-(2*b)
    if(x<y):
       print("FIRST")
    elif(x>y):
        print("SECOND")
    else:
       print("BOTH")