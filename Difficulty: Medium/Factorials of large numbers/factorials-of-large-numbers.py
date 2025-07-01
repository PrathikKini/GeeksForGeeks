#User function Template for python3

class Solution:
    def factorial(self, n):
        #code here
        fact = 1
        for i in range(1,n+1):
            fact*=i
        return [i for i in str(fact)]