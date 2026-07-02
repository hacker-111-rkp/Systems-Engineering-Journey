
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
#in this we can also use swap with last element or building a new list which does not contain val value 
class Solution(object):
    def removeElement(self, nums, val):
        ans = []

        for num in nums:
            if num != val:
                ans.append(num)

        for i in range(len(ans)):
            nums[i] = ans[i]

        return len(ans)


#------------------------------------------
class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1

        return n



