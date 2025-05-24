#User function Template for python3

class Solution:
    def modify(self, N):
        #code here
        s = str(N)
        l = [s[0]]
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                l.append(s[i])
        return "".join(l)