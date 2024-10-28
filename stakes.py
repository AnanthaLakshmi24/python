#sATACKS
l=[]
n=6
m=list(map(int,input().split()))
for i in range(len(m)):
  if len(l)<=n:
    l.append(m[i])
  else:
    break
print(l)