#User function Template for python3

class Solution:
    def fibonacci(self,n):
        #code here
        return self.fibonacci(n-1) + self.fibonacci(n-2) if n > 1 else n