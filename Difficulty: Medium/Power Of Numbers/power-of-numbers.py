class Solution:
    def reverse_exponentiation(self, n):
        # code here
        return n**int(str(n)[::-1])