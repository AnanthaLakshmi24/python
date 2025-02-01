# cook your dish here
def trail(n):
    count=0
    while(n>0):
        count+=n//5
        n//=5 
    print(count)
t=int(input())
while(t):
    n=int(input())
    trail(n)
    t-=1 