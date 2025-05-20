#User function Template for python3
class Solution:
	def isSame(self, s):
		# code here
        lenS = 0
        n = len(s)
        for ch in s:
            if ch.isdigit():
                break
            lenS+=1
        return 1 if lenS == int(s[lenS:]) else 0