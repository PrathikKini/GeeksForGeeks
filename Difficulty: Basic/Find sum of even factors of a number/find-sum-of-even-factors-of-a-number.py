#User function Template for python3

class Solution:
    def evenFactors (self, N):
        # code here
        total = 0
        for i in range(2,N+1,2):
            if N % i == 0:
                total+=i
        return total