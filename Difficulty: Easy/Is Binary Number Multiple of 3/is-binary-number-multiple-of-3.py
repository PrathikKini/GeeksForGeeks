#User function Template for python3
class Solution:
	def isDivisible(self, s):
		# code here
		mod = 0
		for ch in s:
		    mod = (mod * 2 + int(ch)) % 3
		return mod == 0