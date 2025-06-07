#User function Template for python3


class Solution:
    def firstElementKTime(self, arr,k):
        # code here
        dict_val = {}
        for num in arr:
            dict_val[num] = 1 + dict_val.get(num,0)
            if dict_val[num] == k:
                return num
        return -1
    
