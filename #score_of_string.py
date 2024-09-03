# s="abcd"
# n=len(s)
# for i in range(n-1):
#     print(s[i]+s[i+1])


s="abcd"
ans=0
for i in range(len(s)-1):
    a=ord(s[i])
    b=ord(s[i+1])
    temp=abs(a-b)
    ans=ans+temp

print(ans)