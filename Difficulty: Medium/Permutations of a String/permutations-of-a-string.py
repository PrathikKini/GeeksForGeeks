#User function Template for python3

class Solution:
    def findPermutation(self, s):
        # Code here
        def backtrack(start):
            if start == len(chars):
                result.append("".join(chars))
                return
            
            seen = set()
            for i in range(start,len(chars)):
                if chars[i] in seen:
                    continue
                seen.add(chars[i])
                
                chars[start],chars[i] = chars[i], chars[start]
                backtrack(start+1)
                chars[start],chars[i] = chars[i], chars[start]
            
            
        result = []
        chars = list(s)
        backtrack(0)
        return result
