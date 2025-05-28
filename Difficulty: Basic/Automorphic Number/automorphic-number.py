#User function Template for python3

class Solution:
	def is_AutomorphicNumber(self, n):
		# Code here
		if str(n*n)[-1] == str(n)[-1]:
		    return "Automorphic"
		return "Not Automorphic"
