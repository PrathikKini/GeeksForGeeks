#User function Template for python3

class Solution:
	def is_StrongNumber(self, n):
		# Code here
		def factorial(num):
            result = 1
            for i in range(2,num+1):
                result *= i
            return result
        
        original = n
        sum_of_digit = 0
        while n > 0:
            digit = n % 10
            sum_of_digit += factorial(digit)
            n //= 10
        return 1 if original == sum_of_digit else 0