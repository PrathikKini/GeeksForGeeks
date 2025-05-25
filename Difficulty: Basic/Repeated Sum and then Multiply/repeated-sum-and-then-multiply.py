#User function Template for python3
class Solution:
    def repeatedSumMul (self, n):
        # code here 
        lasttwodigit = 10 
        
        while n>=10:
            if 10 <= n <= 99:
                lasttwodigit = n
            n = sum([int(num) for num in str(n)])
            
        digit = [int(num) for num in str(lasttwodigit)]
        return digit[0] * digit[1] 