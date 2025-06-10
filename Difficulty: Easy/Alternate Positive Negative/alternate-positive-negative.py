#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        pos_num = [i for i in arr if i>=0]
        neg_num = [i for i in arr if i<0]
        result = []
        
        for pos,neg in zip(pos_num,neg_num):
            result.append(pos)
            result.append(neg)
            
        result.extend(pos_num[len(neg_num):])
        result.extend(neg_num[len(pos_num):])
        
        for i in range(len(arr)):
            arr[i] = result[i]