#tough one 
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
        return atmost(goal)-atmost(goal-1)# as atmost(2)-->0,1,2 includes all subarrays but atmost(1)-->include 0,1 subarray 
        #so for window==2 in ex 1) stmost(2)-atmost(1)
        
