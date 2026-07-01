class Solution(object):
    def findNumbers(self, nums):
        count=0
        for i in nums:
            if len(str(i))%2==0:
                count+=1
        return count
sol=Solution()
print(sol.findNumbers([55,66,234,222222]))
"""Time Complexity:O(Nk), where N is the number of elements and k is the number of digits
in the numbers (due to string conversion).Space Complexity: O(K) to store the string representation of the current number."""

#mathematical approach 

def findNumbers(nums):
    count = 0
    for num in nums:
        num = abs(num)
        digits = 0
        while num > 0:
            num //= 10
            digits += 1
        if digits % 2 == 0:
            count += 1
    return count
"""Time Complexity:O(Nk) where K is the number of digits.
Space Complexity: O(1) (no extra storage like strings).
"""
#log approach 
import math
def findNumbers(nums):
    count = 0
    for num in nums:
        if num == 0: continue # 0 has 1 digit (odd)
        # log10(abs(num)) gives the power of 10
        digits = int(math.log10(abs(num))) + 1
        if digits % 2 == 0:
            count += 1
    return count
"""
Time Complexity: O(N), as calculating log_{10} is effectively O(1).
Space Complexity: O(1).
"""
