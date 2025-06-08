#User function Template for python3

class Solution:
    def minValue(self, arr1, arr2):
        #code here
        arr1.sort()
        arr2.sort(reverse=True)
        return sum([a1*a2 for a1,a2 in zip(arr1,arr2)])
        
