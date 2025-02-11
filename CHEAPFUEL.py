# cook your dish here
# cook your dish here
t=int(input())
for i in range(t):
    x, y, a, b, k=map(int, input().split())
    nx=x+k*a
    ny=y+k*b
    if(nx<ny):
        print("PETROL")
    elif(ny<nx):
        print("DIESEL")
    else:
        print("SAME PRICE")