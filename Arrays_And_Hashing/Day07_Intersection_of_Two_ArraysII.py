#sorting + two pointers 
#TC--O(N) , SC--O(N+M)
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        left,right=0,0
        ans=[]
        while left<len(nums1) and right < len(nums2):
            if nums1[left]<nums2[right]:
                left+=1
            elif nums1[left]>nums2[right]:
                right+=1
            else:
                ans.append(nums1[left])
                left+=1
                right+=1
        return ans 
sol=Solution()
print(sol.intersect([9,4,4,9,8,4],[4,9,5]))
#hashmap
#TC--O(n+m) , SC--O(n)
class Solution(object):
    def intersect(self, nums1, nums2):
        h={}
        ans=[]
        for i in nums1:
            h[i]=h.get(i,0)+1
        for j in nums2:
            if j in h and h[j]>0:
                ans.append(j)
                h[j]-=1
        return ans
        
sol=Solution()
print(sol.intersect([9,4,4,9,8,4],[4,9,5]))
