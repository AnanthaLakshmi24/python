# cook your dish here
x,y = map(eval,input().split())
if x+0.50<=y:
    if x%5==0:
        print(y-(x+0.50))
    elif x%5!=0:
        print(y)
else:
    print(y)