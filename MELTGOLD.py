# cook your dish here
t=int(input())
for i in range(t):
    melt,ini=map(int,input().split())
    i=0
    while(ini<=melt):
        i+=1
        ini+=i
    print(i)
	   
	   