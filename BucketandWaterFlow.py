# cook your dish here
t=int(input())
for i in range(t):
    a,x,b,c=map(int,input().split())
    k=a+(b*c)
    if x<k:
        print("overflow")
    elif x==k:
        print("filled")
    else:
        print("Unfilled")