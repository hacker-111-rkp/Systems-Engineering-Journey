# two pointers manually
#TC--O(N),SC--O(N)
class Solution(object):
    def reverseWords(self, s):
        res = []
        i = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] == " ":
                i -= 1
            if i < 0:
                break
            j = i
            while j >= 0 and s[j] != " ":
                j -= 1
            res.append(s[j + 1:i + 1])
            i = j
        return " ".join(res)
# BUILD IN FUNCTION
#TC--O(N),SC--O(N)
class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)
