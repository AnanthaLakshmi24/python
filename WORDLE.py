# cook your dish here
t=int(input())
for i in range(t):
    s=input()
    T=input()
    li=[]
    for j in range(len(s)):
        if s[j]==T[j]:
            li.append("G")
        else :
            li.append("B")
    def convert(li):
        new=""
        for x in li:
            new=new+x  
        return new
    print(convert(li))
        