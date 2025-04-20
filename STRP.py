# cook your dish here
t = int(input())
for _ in range(t):
    n =int(input())
    s = input()
    cnt = 0
    
    i = 0
    while(i<len(s)-1):
        if s[i]==s[i+1]:
            i+=2
            n-=1
        else:
            i+=1 
            
    print(n)
        
            
        
            
            
        
