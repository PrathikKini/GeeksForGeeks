#User function Template for python3

class Solution:
    def printSeries(self, N):
    	#code here 
    	series = [1,2,5]
    	for i in range(3,N):
    	    next_term = series[-1] + series[-2] + series[-3]
    	    series.append(next_term)
    	return series[:N]