#User function Template for python3

class Solution:
    def sumOfNaturals(self, n):
        # code here 
        if n == 0:
            return 0
        return sum([i for i in range(1,n+1)])