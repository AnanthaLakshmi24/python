def checkPerfectNumber(num: int) -> bool:
    sum_factors = 1
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            sum_factors += i + (num // i)
    
    return sum_factors == num  
num = int(input())
if checkPerfectNumber(num):
    print("YES")
else:
    print("NO")
