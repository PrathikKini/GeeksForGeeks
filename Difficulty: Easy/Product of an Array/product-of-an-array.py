class Solution:
    # arr is the array
    def product(self, arr):
        # your code here
        res = 1
        for i in arr:
            res*=i
        if res < 1000000007:
            return res
        return res % 1000000007