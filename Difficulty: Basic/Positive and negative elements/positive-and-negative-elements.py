#User function Template for python3



class Solution:
    def arranged(self,arr):
        #Code here
        pos = [x for x in arr if x > 0]
        neg = [x for x in arr if x < 0]
        
        result = []
        for p,n in zip(pos,neg):
            result.append(p)
            result.append(n)
        return result