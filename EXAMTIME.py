# cook your dish here
t=int(input())
for i in range(t):
    dsa,toc,dm=map(int,input().split())
    dsa1,toc1,dm1=map(int,input().split())
    dragon=dsa+toc+dm 
    sloth=dsa1+toc1+dm1
    if  dragon>sloth:
        print("DRagon")
    elif dragon<sloth:
        print("SLOTH")
    else:
        if dsa>dsa1:
            print("DRAGON")
        elif dsa<dsa1:
            print("sLOTH")
        elif dsa==dsa1:
            if toc>toc1:
                print("DRAGON")
            elif toc<toc1:
                print("SLOTH")
            else:
                print("TIE")