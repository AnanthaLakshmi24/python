#merge sort
l=list(map(int,input().split()))

def combine(l,start,mid,end):
  left=l[start:mid+1]
  right=l[mid+1:end+1]
  i,j=0,0
  result=[]
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      result.append(left[i])
      i=i+1
    else:
      result.append(right[j])
      j=j+1
  while i<len(left):
    result.append(left[i])
    i=i+1
  while j<len(right):
    result.append(right[j])
    j=j+1
  l[start:end+1]=result[:]

def divide(l,start,end):
  if start<end:
    mid=(start+end)//2
    divide(l,start,mid)
    divide(l,mid+1,end)
    combine(l,start,mid,end)

divide(l,0,len(l)-1)
print(l)

