class Solution:
    def canSplit(self, arr):
        #code here
        arr_sum = sum(arr)
        if arr_sum % 2 != 0:
            return False
        
        curr_sum = 0
        target = arr_sum // 2
        
        for num in arr:
            curr_sum += num
            if target == curr_sum:
                return True
        return False