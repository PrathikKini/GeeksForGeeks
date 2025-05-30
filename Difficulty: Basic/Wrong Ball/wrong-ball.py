#User function Template for python3

class Solution:
    def countWrongPlacedBalls(self, s):
        # code here
        cnt = 0
        for i in range(0,len(s),2):
            if s[i] == 'B':
                cnt+=1
        for i in range(1,len(s),2):
            if s[i] == 'R':
                cnt+=1
        return cnt