n=int(input())
even=0
odd=0
while n!=0:
    rem=n%10
    if rem%2==0:
        even=even+1
    else:
        odd=odd+1
    n=n//10
print(even,"even no. of digits")
print(odd,"odd number of digits")