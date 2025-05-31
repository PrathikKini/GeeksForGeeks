
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return b
