address='[1.1.1.1]'
ans=''
for i in address:
    if i == '.':
        ans=ans+"[.]"
    else:
        ans=ans+i
print(ans)
            