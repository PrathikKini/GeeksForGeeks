#User function Template for python3
from math import sqrt
class Solution:
    def isPerfectNumber(self, n):
        # code here 
        if n < 2:
            return False
        s = 1
        for i in range(2,int(sqrt(n)+1)):
            if n % i == 0:
                s = s+i+(n//i if i!=n//i else 0)
            if s == n:
                return True
        return False
                