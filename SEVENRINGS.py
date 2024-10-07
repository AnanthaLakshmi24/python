t = int(input())

while t > 0:
    n, x = map(int, input().split())
    # Your code goes here
    m=n*x 
    c=0
    while m!=0:
        rem=m%10
        c=c+1 
        m=m//10
    
    if c==5:
        print("YES")
    else:
        print("NO")
    
    t -= 1
