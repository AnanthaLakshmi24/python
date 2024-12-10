# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    ans=""
    for si in range(n):
        if s[si]=="A":
            ans=ans+"T"
        elif s[si]=="T":
            ans+="A" 
        elif s[si]=="G":
            ans=ans+"C"
        else:
            ans+="G"
    print(ans)
        