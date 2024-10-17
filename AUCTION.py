# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x>y and x>z:
        print("Alice")
    elif y>x and y>z:
        print("Bob")
    else:
        print("Charlie")