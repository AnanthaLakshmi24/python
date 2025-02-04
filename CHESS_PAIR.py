# cook your dish here
for i in range(int(input())):
    N,X=map(int,input().split())
    if(X > ((2*N)-X)):
        print(X-((2*N)-X))
    else:
        print(0)