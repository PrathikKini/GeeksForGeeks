import bisect
class Solution:
    def lis(self, arr):
        # code here
        sub = []
        for num in arr:
            i = bisect.bisect_left(sub,num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)