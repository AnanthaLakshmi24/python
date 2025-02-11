# cook your dish here
ball=int(input())
for b in range(ball):
  p=list(map(int,input().split()))
  p1=sum(p[0::2])
  p2=sum(p[1::2])
  if p1>p2: print(1)
  elif p1<p2: print(2)
  else: print(0)