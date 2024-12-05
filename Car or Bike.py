# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>y:
        print("CAR")
    elif x<y:
        print("BIKE")
    else:
        print("SAME")