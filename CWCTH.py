# cook your dish here
# Read input values
A, B = map(int, input().split())

# Check the condition
if B >= 3 * A:
    print("Rain")
else:
    print("Dry")
