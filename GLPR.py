# cook your dish here
x,y=map(int,input().split())
price=2*x 
if price>=y:
    print("METAL")
else:
    print("PLASTIC")