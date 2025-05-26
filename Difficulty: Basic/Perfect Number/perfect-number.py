#User function Template for python3

class Solution:
    def isPerfect(self,N):
        #code here
        def fact(n):
            result = 1
            for i in range(2,n+1):
                result *= i
            return result
        
        return 1 if sum(fact(int(i)) for i in str(N)) == N else 0