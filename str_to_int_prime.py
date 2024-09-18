def prime(n):
  if n<=1:
    return False
  for i in range(2,n):
    if n%i==0:
      return False
  return True

s=list(map(str,input().split()))
for i in range(len(s)):
  n=int(s[i])
  if prime(n):
    print(n,end=" ")