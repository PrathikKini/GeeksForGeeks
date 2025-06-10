class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # code here
        if arr == sorted(arr):
            return True
        return False