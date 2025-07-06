#User function Template for python3

class Solution:

    def sameChar(self, A, B):
        # code here
        l_a = A.lower()
        l_b = B.lower()
        cnt = 0
        for a,b in zip(l_a,l_b):
            if a == b:
                cnt+=1
        return cnt
