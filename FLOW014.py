# cook your dish here
T = int(input())

# Iterate through each test case
for _ in range(T):
    hardness, carbon_content, tensile_strength = map(float, input().split())
    
    # Check the conditions
    cond1 = hardness > 50
    cond2 = carbon_content < 0.7
    cond3 = tensile_strength > 5600
    
    # Determine grade
    if cond1 and cond2 and cond3:
        grade = 10
    elif cond1 and cond2:
        grade = 9
    elif cond2 and cond3:
        grade = 8
    elif cond1 and cond3:
        grade = 7
    elif cond1 or cond2 or cond3:
        grade = 6
    else:
        grade = 5
    
    # Print the grade
    print(grade)