#User function Template for python3

class Solution:
    
    #Function to check if the number is sparse or not.
    def isSparse(self,n):
        #Your code here 
        return 1 if (n & (n >> 1)) == 0 else 0
