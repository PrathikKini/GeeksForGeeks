#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        return True if n == sum([int(i)**3 for i in str(n)]) else False 