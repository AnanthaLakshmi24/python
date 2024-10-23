# cook your dish here
t=int(input())
for j in range(t):
    x,y=map(int,input().split())
    Sa=input()
    Sb=input()
    def name(Sa,Sb):
        A=set(Sa)
        B=set(Sb)
        
        all_char=set("abcdefghijklmnopqrstuvwxyz")
        
        avail_char=all_char-(A.union(B))
        
        return len(avail_char)
    
    res=name(Sa,Sb)
    if res>0:
        print("Yes")
    else:
        print("No")