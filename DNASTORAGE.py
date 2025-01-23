t = int(input())

while t > 0:
    n = int(input())
    h = input()
    z=""
    # Your code goes here
    for j in range(0,n,2):
        if(h[j]+h[j+1]=="00"):
            z=z+"A"
        elif(h[j]+h[j+1]=="01"):
            z=z+"T"
        elif(h[j]+h[j+1]=="10"):
            z=z+"C"
        else:
            z=z+"G"
    print(z)
    
    t -= 1
