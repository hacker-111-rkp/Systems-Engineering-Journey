class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix=0
        h={0:-1}
        for i in range(len(nums)):
            prefix+=nums[i]
            rem=prefix%k
            if rem in h:
                if i-h[rem]>=2:
                    return True
            else:
                h[rem]=i
        return False

