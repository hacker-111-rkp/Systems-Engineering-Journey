class Solution(object):
    def findMaxConsecutiveOnes(self,nums):
        max_count=0
        count=0
        for i in nums:
            if i==1:
                count+=1
            else:
                if max_count<count:
                    max_count=count
                count=0
        return max(max_count,count)
sol=Solution()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))


#tc--o(n)
#sc -- o(1)
