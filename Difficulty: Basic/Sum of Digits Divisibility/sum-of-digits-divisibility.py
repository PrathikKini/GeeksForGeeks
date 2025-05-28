#User function Template for python3

class Solution:
    def isDivisible(self,N):
        #code here
        digit_sum = sum(int(i) for i in str(N))
        return 1 if N % digit_sum == 0 else 0
            