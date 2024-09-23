l=[-4,-1,2,4,6,8,10,47]
low = 0
high = len(l)-1
c=0
key=20
while low<=high:
    m = (low+high)//2
    if l[m]==key:
        print("Element Found")
        c=1
        break
    elif l[m]>key:
        high = m - 1
    else:
        low = m+1
if c==0:
    print("Element not Found")
