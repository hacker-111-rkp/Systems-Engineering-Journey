
#brute force 
result = []

for x in nums1:
    for y in nums2:
        if x == y and x not in result:
            result.append(x)

#hashset
class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1)&set(nums2))
sol=Solution()
print(sol.intersection([1,2,2,1],[2,2]))

#hashset with better space 
seen = set(nums1)
answer = set()

for x in nums2:
    if x in seen:
        answer.add(x)

return list(answer)
#hashmap
freq = {}

for x in nums1:
    freq[x] = 1

answer = []

for x in nums2:
    if x in freq:
        answer.append(x)
        del freq[x]
#sorting + two pointers 
#O(n log n + m log m) , sc --o(1)
nums1.sort()
nums2.sort()

i = j = 0
ans = []

while i < len(nums1) and j < len(nums2):

    if nums1[i] < nums2[j]:
        i += 1

    elif nums1[i] > nums2[j]:
        j += 1

    else:

        if not ans or ans[-1] != nums1[i]:
            ans.append(nums1[i])

        i += 1
        j += 1

return ans
