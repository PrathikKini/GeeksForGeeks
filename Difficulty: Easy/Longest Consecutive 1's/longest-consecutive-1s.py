class Solution:
    def maxConsecutiveOnes(self, N):
        #code here
        return max(map(len,bin(N)[2:].split('0')))


