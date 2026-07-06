#TC--O(2n)--O(n)
#SC--O(1)
class Solution(object):
    def  removeDuplicates(self,nums):
        left=1
        if not nums:
            return 0
        for right in range(1,len(nums)):
            if nums[right-1]!=nums[right]:
                nums[left]=nums[right]
                left+=1
        return left
        
sol=Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,3,4,5]))


# by using index method 
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        write = 0

        for num in nums:
            if nums[write] != num:
                write += 1
                nums[write] = num

        return write + 1

#TC--O(n)
#SC--O(1)
