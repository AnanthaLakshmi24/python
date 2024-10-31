# cook your dish here
t=int(input())
for i in range(t):
    d,l,r=map(int,input().split())
    if (d>=l and d<=r):
        print("Take second dose now")
    
    elif (d >l and d > r):
        print("Too Late")
    
    else :
        print("Too Early")
        