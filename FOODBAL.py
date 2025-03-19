# cook your dish here
a,b,c,d=map(int,input().split())
k=abs(a-b)
t=abs(c-d)
if k<t:
    print('first')
elif k==t:
    print('both')
else:
    print('second')
