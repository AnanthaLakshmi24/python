# cook your dish here
t=int(input()) 
l=[1,2,4,8,16,32,64,128,256,512,1024,2048]
for _ in range(t):
    p=int(input())
    i=len(l)-1 
    c=0 
    while(i>=0 and p!=0):
        if l[i] > p:
            i-=1 
        else:
            p=p-l[i] 
            c+=1 
    print(c) 
    
    