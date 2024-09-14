
from abc import ABC,abstractmethod
import math

class polygon(ABC):
  @abstractmethod
  def area(Self):
    pass

    @abstractmethod
    def perimeter(Self):
      pass

class Triangle(polygon):
  def __init__(self,a,b,c):
    self.a=a
    self.b=b
    self.c=c

  def area(self):
    s=self.perimeter()/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

  def perimeter(self):
    return self.a + self.b + self.c

class Quadrilateral(polygon):
#Assume quadrilateral as a Rectangle for simplicity
  def __init__(self,a,b):
    self.a=a
    self.b=b

  def area(self):
    return self.a*self.b

  def perimeter(self):
    return 2*(self.a+self.b)

class Pentagon(polygon):
  def __init__(self,side):
    self.side=side

  def area(self):
    return (1/4)*math.sqrt(5*(5+2*(math.sqrt(5)))) * self.side**2

  def perimeter(self):
    return 5 * self.side

while True:
  print("\nChoose a polygon:")
  print("1.Triangle")
  print("2.Quadrilateral")
  print("3.Pentagon")
  print("4.Exit")

  choice=input("Enter your choice(1-4):")

  if(choice=="1"):
    a=float(input("Enter side a:"))
    b=float(input("Enter side b:"))
    c=float(input("Enter side c:"))
    triangle=Triangle(a,b,c)
    print(f"Area of triangle is : {triangle.area():.2f}")
    print(f"Perimeter of triangle is : {triangle.perimeter():.2f}")


  elif choice=="2":
     a=float(input("Enter side a:"))
     b=float(input("Enter side b:"))
     quadrilateral=Quadrilateral(a,b)
     print(f"Area of quadrilateral is : {quadrilateral.area():.2f}")
     print(f"Perimeter of quadrilateral is : {quadrilateral.perimeter():.2f}")


  elif choice=="3":
    side=float(input("Enter side:"))
    pentagon=Pentagon(side)
    print(f"Area of pentagon is: {pentagon.area():.2f}")
    print(f"perimeter of pentagon is : {pentagon.perimeter():.2f}")


  elif choice=="4":
    break

  else:
    print("Invalid choice.Please try again")


#23A91A0485
#G.D.A.Lakshmi

