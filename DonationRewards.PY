# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if x<=3:
        print("BRONZE")
    elif x>3 and x<=6:
        print("SILVER")
    else:
        print("GOLD")