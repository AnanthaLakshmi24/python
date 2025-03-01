# cook your dish here
for i in range (int(input())):
    x=list(map(int,input().split()))
    count=sum(x)
    if(count==0):
        print("Beginner")
    elif(count==1):
        print("Junior Developer")
    elif(count==2):
        print("Middle Developer")
    elif(count==3):
        print("Senior Developer")
    elif(count==4):
        print("Hacker")
    else:
        print("Jeff Dean")