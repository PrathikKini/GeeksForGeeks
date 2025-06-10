#User function Template for python3

class Solution:
    def filterByDigits(self, arr):
        #code here
        result = []
        allowed_digit = {'1','2','3'}
        
        for num in arr:
            if all(digit in allowed_digit for digit in str(num)):
                result.append(num)
        return result