#User function Template for python3

class Solution:
    def countPairs(self,arr1, arr2, x):
        #code here.
        i = 0
        j = len(arr2) - 1
        count = 0
        
        while i < len(arr1) and j >= 0:
            total = arr1[i] + arr2[j]
            if total == x:
                count+=1
                i += 1
                j -= 1
            elif total < x:
                i += 1
            else:
                j -= 1
        return count