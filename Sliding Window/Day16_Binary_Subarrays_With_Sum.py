class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def atmost(goal):
            if goal<0:
                return 0
            left=0
            window=0
            count=0
            for right in range(len(nums)):
                window+=nums[right]
                while window>goal:
                    window-=nums[left]
                    left+=1            
                count += (right - left + 1)
            return count
        return atmost(goal)-atmost(goal-1)
        
