class Solution:
    def majorityElement(self, arr):
        #code here
        dict = {}
        for num in arr:
            dict[num] = 1 + dict.get(num,0)
        
        size = len(arr) // 2
        for k,v in dict.items():
            if v > size:
                return k
        return -1