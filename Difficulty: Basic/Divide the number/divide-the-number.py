#User function Template for python3
import math
class Solution:
    def countWays (self, N):
        # code here
        res = 0
        if N < 4:
            return 0
            
        for n1 in range(1,N):
            for n2 in range(n1,N):
                for n3 in range(n2,N):
                    if N - n1 - n2 -n3 >= n3:
                        res+=1
                    else:
                        break
        return res