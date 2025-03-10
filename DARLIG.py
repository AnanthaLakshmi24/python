# cook your dish here
for i in range(int(input())):
    A,B=map(int,input().split())
    if B==0:
        if (A%4==0):
            print("Off")
        else:
            print("On")
    else:
        if (A%4!=0):
            print("Ambiguous")
        else:
            print("on")