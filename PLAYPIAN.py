# cook your dish here
for _ in range(int(input())):
    y = input()
    f = True
    for i in range(0,len(y),2):
        if(y[i]==y[i+1]): f = False 
    if(f): print("yes")
    else: print("no")