#User function Template for python3
class Solution:
    def checkPerfectSquare (ob,N):
        # code here 
        i = 1
        while N > 0:
            N -= i
            i += 2
        return 1 if N == 0 else 0