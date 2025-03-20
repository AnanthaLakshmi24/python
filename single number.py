from typing import List

def singleNumber(nums: List[int]) -> int:
    xor = 0
    for num in nums:
        xor ^= num
    return xor

nums = list(map(int, input().split()))
result = singleNumber(nums) 
print(result)
