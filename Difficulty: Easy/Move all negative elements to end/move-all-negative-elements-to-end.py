#User function Template for python3

class Solution:
    def segregateElements(self, arr):
        # Your code goes here
        n = len(arr)
        tmp = arr.copy()
        pos_index = 0
        
        for i in range(n):
            if tmp[i] >= 0:
                arr[pos_index] = tmp[i]
                pos_index += 1
            
        for i in range(n):
            if tmp[i] < 0:
                arr[pos_index] = tmp[i]
                pos_index += 1
                