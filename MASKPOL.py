# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    z=a-b
    print(min(z,b))