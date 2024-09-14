print("*"*50)
print("\t Print color")
print("*"*50)
print("\t Violet")
print("\t Indigo")
print("\t Blue")
print("\t Green")
print("\t Yellow ")
print("\t Orange")
print("\t Red")
print("*"*50)
print("enter the choice:")
choice=(input())
match(choice):
  case "V":
    print("V-> voilet")
  case "B":
    print("B -> Blue")
  case "G":
    print("G -> Green")
  case "Y":
    print("Y -> Yellow")
  case "O":
    print("O -> Orange")
  case "R":
    print("R -> Red")
  case _:
    print("you enter invalid colour")
