# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    chick=(z%x==0)
    duck=(z%y==0)
       
    if (chick and duck):
        print("ANy")
    elif(chick):
        print("CHICKEN")
    elif(duck):
        print("DUCK")
    else:
        print("NONE")