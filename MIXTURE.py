# cook your dish here
t=int(input())
for i in range(t):
    s,l=map(int,input().split())
    if s>0 and l>0:
        print("Solution")
    elif s==0:
        print("Liquid")
    elif l==0:
        print("Solid")