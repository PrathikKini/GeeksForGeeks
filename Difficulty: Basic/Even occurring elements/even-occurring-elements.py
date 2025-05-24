class Solution:
    def findEvenOccurrences(self, arr):
        # code here
        freq = {}
        for i in arr:
            freq[i] = 1 + freq.get(i,0)
        
        evens = [k for k,v in freq.items() if v%2 == 0]
        return evens if evens else [-1]
