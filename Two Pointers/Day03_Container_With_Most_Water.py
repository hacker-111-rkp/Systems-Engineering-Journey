class Solution:
    def maxArea(self, heights):
        left,right=0,len(heights)-1 
        max_area=0
        while left<right:
            area=min(heights[left],heights[right])*(right-left)
            max_area=max(max_area,area)
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return max_area
    
sol=Solution()
print(sol.maxArea([1,7,2,5,4,7,3,6]))
        
