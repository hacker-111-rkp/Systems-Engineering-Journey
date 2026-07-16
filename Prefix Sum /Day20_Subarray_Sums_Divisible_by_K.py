class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        h={0:1}
        prefix=0
        count=0
        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix%k in h:
                count+=h[prefix%k]
            h[prefix%k]=h.get(prefix%k,0)+1
        return count
