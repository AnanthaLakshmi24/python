print("*"*50)
print("\t Airthemetic operations")
print("*"*50)
print("\t 1.Addition")
print("\t 2.Subtraction")
print("\t 3.Multiplication")
print("\t 4.Division")
print("\t 5.Floor division")
print("\t 6.Modulo division")
print("\t 7.power")
print("*"*50)
print("enter the choice:")
choice=int(input())
match(choice):
  case 1:
    print("enter two values for Addition operation")
    a,b=map(int,input().split())
    c=a+b
    print(c)
  case 2:
    print("enter two values for Subtraction operation")
    a,b=map(int,input().split())
    c=a-b
    print(c)
  case 3:
    print("enter two values for Multiplication operation")
    a,b=map(int,input().split())
    c=a*b
    print(c)
  case 4:
    print("enter two values for division operation")
    a,b=map(int,input().split())
    c=a/b
    print(c)
  case 5:
    print("enter two values for float division operation")
    a,b=map(int,input().split())
    c=a//b
    print(c)
  case 6:
    print("enter two values for Modulo Division  operation")
    a,b=map(int,input().split())
    c=a+b
    print(c)
  case 7:
    print("enter two values for power operation")
    a,b=map(int,input().split())
    c=a+b
    print(c)
  case _:
   print("You enter invalid operator")