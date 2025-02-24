# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a1=input()
    a2=input()
    r=[] 
    for j in range((x-y)+1):
        new=a1[j:j+y]
        cnt=0
        for k in range(y):
            if new[k]!=a2[k]:
                cnt+=1
        r.append(cnt)
    print(min(r))