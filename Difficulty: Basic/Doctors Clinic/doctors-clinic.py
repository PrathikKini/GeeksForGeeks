#User function Template for python3

class Solution:
    def waitingTime(self, N, X):
        # code here
        return max(0,(N-1) * (10 - X))