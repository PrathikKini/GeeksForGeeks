#User function Template for python3
class Solution:
    def nisDoryOrNot (ob, n):
        # code here 
        x = 5 * n - 4
        y = 5 * n + 4
        x1 = int(x**0.5)
        y1 = int(y**0.5)
        if x1*x1 == x or y1*y1 == y:
            return 1
        return 0