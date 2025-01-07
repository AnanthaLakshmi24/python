# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    for k in range(1,100):
        if x%k!=0 and y%k!=0 and z%k!=0:
            print(k)
            break