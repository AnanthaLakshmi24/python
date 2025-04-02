# cook your dish here
t=int (input())
for i in range(t):
    a,b,c=map(int,input().split())
    
    if(a>50 and a>b and a>c):
        print('A')
    elif(b>50 and b>a and b>c):
        print('B')
    elif(c>50 and c>a and c>b):
        print('c')
    else:
        print('NOTA')
        
        
