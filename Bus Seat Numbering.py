# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    if x>=1 and x<=10:
        print("Lower Double")
    elif x>=11 and x<=15:
        print("Lower Single")
    elif x>=16 and x<=25:
        print("Upper Double")
    else:
        print("Upper Single")
    