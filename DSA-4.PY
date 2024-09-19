

# List Comprehensions
squares = [ x**2 for x in range (10)]
print("List comprehension (squares):",squares)

# Dictionary Comprehensions
square_dict = { x:x**2 for x in range (10)}
print("Dictionary comprehension(squares):",square_dict)

# Set Comprehensions
unique_squares = {x**2 for x in range (10)}
print("Set comprehension (unique squares):",unique_squares)

# Generator comprehensions
squares_gen = (x**2 for x in range (10))
mg=list(squares_gen)
print("Generator Comprehension (squares):",mg)
print (list(squares_gen))
print(mg)
