#User function Template for python3

class Solution:
    def DivisibleByEight(self,s):
        #code here
        lastthree = s[-3:] if len(s)>3 else s
        if int(lastthree) % 8 == 0:
            return 1
        return -1