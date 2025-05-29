#User function Template for python3
import math
class Solution:
    def findHeightOrDistance(self, type, value, angle):
        #code here
        if type == 'h':
            result = value / math.tan(angle * 3.14/180.0)
        else:
            result = value * math.tan(angle * 3.14/180.0)
        return math.floor(result)