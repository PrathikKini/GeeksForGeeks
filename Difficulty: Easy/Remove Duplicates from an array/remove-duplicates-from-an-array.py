class Solution:
    def remDuplicate(self, arr):
        # code here 
        lst = []
        seen = set()
        for num in arr:
            if num not in seen:
                seen.add(num)
                lst.append(num)
        return lst