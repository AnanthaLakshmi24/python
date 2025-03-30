for _ in range(int(input())):
    N=int(input())
    s=input()
    o=s.count("1")
    z=s.count("0")
    c=0
    if z>=o:
        c=o
    else:
        c=1+z
    print(c)