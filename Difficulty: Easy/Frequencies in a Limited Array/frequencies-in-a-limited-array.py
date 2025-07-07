class Solution:
    def frequencyCount(self, arr):
        #  code here
        n = len(arr)
        freq = [0] * n
        for num in arr:
            if 1 <= num <= n:
                freq[num-1] += 1
        return freq
