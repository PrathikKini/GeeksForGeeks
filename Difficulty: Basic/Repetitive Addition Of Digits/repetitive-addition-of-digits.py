class Solution:
    def singleDigit(self, n):
    	#code here 
    	while n > 9:
    	    n = sum(int(i) for i in str(n))
    	return n