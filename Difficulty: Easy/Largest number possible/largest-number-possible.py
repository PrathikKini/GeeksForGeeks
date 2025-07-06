#User function Template for python3

class Solution:
    def findLargest(self, n, s):
        # code here
        if s > 9 * n or (s == 0 and n > 1):
            return -1
        
        result = ""
        for i in range(n):
            digit = min(9,s)
            result+=str(digit)
            s-=digit
        return result