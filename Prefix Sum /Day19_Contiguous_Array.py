class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        h={0:-1}# at index -1 its prefix value is 0 for other 0 occur its first will be at -1 index to get length 
        prefix=0
        count=0
        for i in range(len(nums)):

            if nums[i]==0:
                prefix-=1
            else:
                prefix+=1
            if prefix in h:
                count=max(count,i-h[prefix])#length = current_index - first_index
            else:
                h[prefix]=i
        return count

