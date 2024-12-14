# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>=1 and x<=10:
        c=1 
    if y>=1 and y<=10:
        d=1 
    if x>=11 and x<=20:
        c=2 
    if y>=11 and y<=20:
        d=2 
    if x>=21 and x<=30:
        c=3 
    if y>=21 and y<=30:
        d=3 
    if x>=31 and x<=40:
        c=4
    if y>=31 and y<=40:
        d=4
    if x>=41 and x<=50:
        c=5
    if y>=41 and y<=50:
        d=5 
    if x>=51 and x<=60:
        c=6
    if y>=51 and y<=60:
        d=6
    if x>=61 and x<=70:
        c=7
    if y>=61 and y<=70:
        d=7 
    if x>=71 and x<=80:
        c=8
    if y>=71 and y<=80:
        d=8
    if x>=81 and x<=90:
        c=9 
    if y>=81 and y<=90:
        d=9
    if x>=91 and x<=100:
        c=10 
    if y>=91 and y<=100:
        d=10 
    print(abs(c-d))