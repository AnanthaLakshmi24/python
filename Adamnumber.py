n=int(input())
def reverse(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10

    return rev

def square(n):
    return n*n
a=square(n)
b=square(reverse(n))
c=reverse(b)

if a==c:
    print("Adam number")
else:
    print("Not Adam Number")