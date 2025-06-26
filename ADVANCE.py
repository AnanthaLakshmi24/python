# cook your dish here
for t in range(int(input())):
    x,y = map(int,input().split())
    if(y>=x and y<=(200+x)):
        print("Yes")
    else:
        print("no")