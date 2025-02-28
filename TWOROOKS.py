# cook your dish here
rook=int(input())
for r in range(rook):
  a,b,c,d=map(int,input().split())
  if a==c or b==d: print("yes")
  else: print("no")