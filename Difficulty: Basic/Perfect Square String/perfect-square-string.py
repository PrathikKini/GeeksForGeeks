#User function Template for python3
import math
class Solution:
    def isSquare(self, S): 
        #code here
        sum = 0
        for v in S:
            sum+=ord(v)
        val = int(math.sqrt(sum))
        if val*val==sum:
            return 1
        return 0


