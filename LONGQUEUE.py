# cook your dish here
t=int(input())
for j in range(t):
    x=int(input())
    l=list(map(int,input().split()))
    half=l[-1]
    c=x-1
    for i in range(x-2,-1,-1):
        if  half //2 <l[i]:
            break
        else:
           c=c-1

    print(c+1)