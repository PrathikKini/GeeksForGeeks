#User function Template for python3

class Solution:
    def isProduct(self, arr, x):
        # code here
        seen = set()
        for num in arr:
            if num == 0:
                if x == 0:
                    return True
                continue
            if x % num == 0 and (x//num) in seen:
                return True
            seen.add(num)
        return False