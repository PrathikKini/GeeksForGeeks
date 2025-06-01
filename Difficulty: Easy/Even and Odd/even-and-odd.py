#User function Template for python3

class Solution:
    def reArrange(self, arr, N):
        # code here 
        even = [arr[i] for i in range(len(arr)) if arr[i] % 2 == 0]
        odd = [arr[i] for i in range(len(arr)) if arr[i] % 2 != 0]
        
        i = 0
        for e in even:
            arr[i]=e
            i+=2            
            
        i = 1
        for o in odd:
            arr[i]=o
            i+=2            
        
        return 1