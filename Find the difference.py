def findTheDifference(s: str, t: str) -> str:
    s = sorted(s) 
    t = sorted(t) 

    for i in range(len(s)): 
        if s[i] != t[i]: 
            return t[i] 
    return t[-1] 
s = input("Enter the first string (s): ").strip()  
t = input("Enter the second string (t): ").strip() 
if len(t) != len(s) + 1:
    print("Invalid input! The second string must have exactly one extra character.")
else:
    print("The extra character is:", findTheDifference(s, t))
