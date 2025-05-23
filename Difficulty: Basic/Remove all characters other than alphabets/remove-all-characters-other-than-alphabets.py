#User function Template for python3

class Solution:
    def removeSpecialCharacter (self, S):
		#code here
		l = []
		for i in S:
		    if i.isalpha():
		        l.append(i)
		if len(l)==0:
		    return -1
		return "".join(l)