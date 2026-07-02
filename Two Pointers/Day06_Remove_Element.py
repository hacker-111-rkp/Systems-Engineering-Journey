
#TC--O(n)
#SC--O(1)

class Solution(object):
    def removeElement(self, nums, val):
        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left
sol=Solution()
print(sol.removeElement([3,3,3,2,2,1,1],3))
