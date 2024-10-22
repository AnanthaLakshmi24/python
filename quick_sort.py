#quicksort
l=list(map(int,input().split()))
def Quicksort(l,start,end):
  pivot=l[end]
  i=start-1
  for j in range(start,end+1):
    if l[j]<pivot:
      i=i+1
      l[i],l[j]=l[j],l[i]

  l[i+1],l[end]=l[end],l[i+1]
  return i+1

def pivot(l,start,end):
  if start<end:
    p=Quicksort(l,start,end)
    pivot(l,start,p-1)
    pivot(l,p+1,end)

pivot(l,0,len(l)-1)
print(l)
