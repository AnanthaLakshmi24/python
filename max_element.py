a=[12,2,45,20,60]
max=0
for i in range(len(a)):
    s=a[i]
    if max<s:
        max=a[i]

print(max)