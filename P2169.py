# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    r=""
    for i in range(n):
        if s[i]=="0":
            r=r+"1"
        elif s[i]=="1":
            r=r+"0"
    print(r)
    