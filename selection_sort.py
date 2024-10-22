#selection sort
l=list( map(int,input().split()))
for i in range(len(l)):
  minimum=l[i]
  index=i
  for j in range(i,len(l)):
    if minimum>l[j]:
      minimum=l[j]
      index=j
      l[i],l[index]=l[index],l[i]
print(l)