#User function Template for python3

class Solution:
    def minX (self, a, b, c, k):
        #complete the function here
        for i in range(k):
            if a*(i**2)+b*i+c >= k:
                return i