# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    k=abs(x-1)
    p=abs(100-x)
    if k>p:
        print("RIGHT")
    else:
        print("LEFT")