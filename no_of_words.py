a=["hi Anu","How are you","Iam glad to see you","Which class are you studying now"]
ans=0
for i in range(len(a)):
    s=a[i]
    temp=1
    for j in range(len(s)):
        ch=s[j]
        if ch==" ":
            temp=temp+1
    ans=max(ans,temp)
print(ans)
        
