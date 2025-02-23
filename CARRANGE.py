# cook your dish here
for i in range (int(input())):
    a,b,c=map(int,input().split())
    fuel=b-(a-1)
    distance=fuel*c
    print(distance)