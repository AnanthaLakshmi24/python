# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    min_value=127
    if x>=min_value:
        z=x//127
        if z>=1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")