#User function Template for python3

from collections import Counter
from itertools import groupby

class Solution:
    def getCount (self,S, N):
        # your code here
        return sum(V == N for V in Counter(c for c, _ in groupby(S)).values())

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s, n = input().split()
    s = str(s)
    n = int(n)
    ob = Solution()
    print (ob.getCount (s, n))

    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends