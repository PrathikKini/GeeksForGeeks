#User function Template for python3
class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, number):
        # code here
        i = 1
        result = 0
        while i <= number:
            result += i*i
            i+=1
        return result