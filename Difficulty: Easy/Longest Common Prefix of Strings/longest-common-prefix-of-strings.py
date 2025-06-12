#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        if not arr:
            return ""
        
        shortest = min(arr,key=len)
        for i,ch in enumerate(shortest):
            for other in arr:
                if other[i] != ch:
                    return shortest[:i]
        return shortest