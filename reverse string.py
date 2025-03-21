def reverse_string(s):
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]  
        left += 1
        right -= 1
    for char in s:
        print(char, end="")  
user_input = input("Enter a string: ")
print("Reversed string:", end=" ")
reverse_string(user_input)
