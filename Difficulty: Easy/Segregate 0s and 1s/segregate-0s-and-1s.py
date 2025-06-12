#User function Template for python3

class Solution:
    def segregate0and1(self, arr):
        # code here
        pos_idx = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[pos_idx] = arr[i]
                pos_idx+=1
                
        for i in range(pos_idx,len(arr)):
            arr[i] = 1
                