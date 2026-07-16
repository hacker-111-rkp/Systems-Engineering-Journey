#do it in py 3 otherwise there will be some issue
import math

class Solution(object):
    def gcdSum(self, nums):
        n = len(nums)
        prefixGcd = [0] * n
        mx = 0
        # Build prefixGcd
        for i in range(n):
            mx = max(mx, nums[i])
            prefixGcd[i] = math.gcd(nums[i], mx)
        # Sort
        prefixGcd.sort()
        # Form pairs
        ans = 0
        left, right = 0, n - 1

        while left < right:
            ans += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans
