class Solution:
    def findUnique(self, arr):
        # code here 
        cnt = {}
        for i in arr:
            cnt[i] = 1 + cnt.get(i,0)
        for k,v in cnt.items():
            if v==1:
                return k