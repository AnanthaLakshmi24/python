# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    sec=1
    if n==1 or n==3:
        print(sec)
        continue
    while True:
        if n==1 or n==3:
            print(sec)
            break
        
        if n>=3:
            n-=2
        else:
            n-=1
        
        sec+=1
        
        
            
        