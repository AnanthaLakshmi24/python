# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    c=0
    for j in range(1,x+1):
        if x%j==0:
           c=c+1;
    if c==2:
        print("yes")
    else:
        print("no")