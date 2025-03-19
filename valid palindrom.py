class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        c = ""  
        for char in s:
            if char.isalnum(): 
                c += char  
        return c == c[::-1] 

s = input()
sol = Solution() 
if sol.isPalindrome(s):
    print("YES")
else:
    print("NO")
