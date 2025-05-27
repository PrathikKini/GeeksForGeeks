#User function Template for python3

class Solution:

    def isGoodString(self, s):
        # code here
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return "NO"
        return "YES"