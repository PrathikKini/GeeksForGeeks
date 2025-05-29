#User function Template for python3

class Solution:
	def closestNo(self, x, n):
		# Code here
		if n == 0:
		    return 0
		q = (x//n)
		lower = n*q
		upper = n*(q+1)
		
		if lower == 0:
		    return upper
		
		if abs(x-lower) < abs(x-upper):
		    return lower
		return upper