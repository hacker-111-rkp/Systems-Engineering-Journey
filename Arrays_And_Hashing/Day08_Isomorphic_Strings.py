#TWO HASH MAP
#TC--O(n),SC--O(n)
class Solution(object):
    def isIsomorphic(self, s, t):
        h1={}
        h2={}
        for c1,c2 in zip(s,t):
            if c1 in h1:
                if h1[c1]!=c2:
                    return False
            else:
                h1[c1]=c2
            if c2 in h2:
                if h2[c2]!=c1:
                    return False
            else:
                h2[c2]=c1
        return True
                
sol=Solution()
print(sol.isIsomorphic("egg","add"))
#ONE HASH + ONE SET
#TC--O(n),SC--O(n)
class Solution(object):
    def isIsomorphic(self, s, t):

        mapping = {}
        used = set()

        for c1, c2 in zip(s, t):

            if c1 in mapping:
                if mapping[c1] != c2:
                    return False

            else:
                if c2 in used:
                    return False

                mapping[c1] = c2
                used.add(c2)

        return True


