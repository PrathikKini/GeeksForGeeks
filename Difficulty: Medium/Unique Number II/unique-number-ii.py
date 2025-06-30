#User function Template for python3

class Solution:
	def singleNum(self, arr):
		# Code here
		counta = {}
		for i in arr:
		    counta[i] = 1 + counta.get(i,0)
		return sorted([k for k,v in counta.items() if v == 1])
