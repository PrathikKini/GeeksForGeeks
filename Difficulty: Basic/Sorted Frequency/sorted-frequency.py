#User function Template for python3

class Solution:
	def freqSorted(self, arr):
		# code here
		count = {}
		for i in arr:
		    count[i] = 1 + count.get(i,0)
		
		l_keys = list(count.keys())
		l_keys.sort()
		sorted_dict = {i:count[i] for i in l_keys}
		for k,v in sorted_dict.items():
		    print(k,v)