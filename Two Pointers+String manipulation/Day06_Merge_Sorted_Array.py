# extra array method 
#tc--O(n+m),sc--O(m+n)
class Solution(object):
    
    def merge(self, nums1, m, nums2, n):
        merge=[]
        i,j=0,0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i+=1
            else:
                merge.append(nums2[j])
                j+=1
        while i<m:
            merge.append(nums1[i])
            i+=1
        while j<n:
            merge.append(nums2[j])
            j+=1
        nums1[:]=merge
sol=Solution()
print(sol.merge([1,2,3,0,0,0],3,[2,3,5],3))
# three pointers backward method 
#tc--O(m+n), sc--O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1          # Last valid element in nums1
        j = n - 1          # Last element in nums2
        k = m + n - 1      # Last position in nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy any remaining elements from nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
