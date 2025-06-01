class Solution:
    def getMaxVal(self, arr, k):
        arr.sort()
        return sum(arr[-k:])