class Solution:
    def firstRepeated(self,arr):
        index_map = {}
        min_index = float('inf')
        
        for i, val in enumerate(arr,1):
            if val in index_map:
                min_index = min(min_index,index_map[val])
            else:
                index_map[val] = i
                
        return min_index if min_index != float('inf') else -1
        