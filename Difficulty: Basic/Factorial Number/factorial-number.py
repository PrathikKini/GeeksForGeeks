#User function Template for python3

class Solution:
    def isFactorial (self, N):
        # code here
        result = 1
        for i in range(1,N+1):
            result*=i
            if result == N:
                return 1
            if result > N:
                return 0
                break