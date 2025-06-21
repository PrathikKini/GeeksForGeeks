#User function Template for python3

class Solution:
	def shortestDistance(self, s, word1, word2):
		# code here
		w1 = [i for i, w in enumerate(s) if w == word1]
		w2 = [i for i, w in enumerate(s) if w == word2]
		return min(abs(i - j) for i in w1 for j in w2)