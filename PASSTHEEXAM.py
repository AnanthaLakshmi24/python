# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    s=x+y+z 
    if s>=100 and x>=10 and y>=10 and z>=10:
        print("PASS")
    else:
        print("FAIL")