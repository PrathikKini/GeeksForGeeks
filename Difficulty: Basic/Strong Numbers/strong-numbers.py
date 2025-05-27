#User function Template for python3

class Solution:
    def isStrong(self, N):
        # code here 
        def factorial(num):
            result = 1
            for i in range(2,num+1):
                result *= i
            return result
        
        original = N
        sum_of_digit = 0
        while N > 0:
            digit = N % 10
            sum_of_digit += factorial(digit)
            N //= 10
        return 1 if original == sum_of_digit else 0