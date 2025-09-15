# cook your dish here
memo = {}

def max_dollars(n):
    if n < 12:
        return n
    if n in memo:
        return memo[n]
    
    memo[n] = max_dollars(n // 2) + max_dollars(n // 3) + max_dollars(n // 4)
    return memo[n]

try:
    while True:
        n = int(input())
        print(max_dollars(n))
except EOFError:
    pass
