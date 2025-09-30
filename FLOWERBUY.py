for _ in range(int(input())):
    n=int(input())
    flag=False
    if(n%3==0):
        print((n//3)*5)
        flag=True
    elif(n%3==1):
        x=((n//3)-1)*5
        print(x+8)
        
    elif(n%3==2):
        x=n//3*5
        print(x+4)
        