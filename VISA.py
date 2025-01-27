# cook your dish here
t=int(input())
for i in range(t):
    x1, x2, y1, y2, z1, z2=map(int, input().split())
    if(x2>=x1 and y2>=y1 and z1>=z2):
        print("yes")
    else:
        print("no")