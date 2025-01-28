# cook your dish here
for t in range(int(input())):
    a,b,c,d=map(int,input().split())
    if(a/c > b/d):
        print('-1')
    elif(a/c<b/d):
        print('1')
    else:
        print('0')