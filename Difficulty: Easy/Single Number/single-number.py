#User function Template for python3

class Solution:
    
    def getSingle(self,arr):
        # code here
        countArr = {}
        for i in arr:
            countArr[i] = countArr.get(i,0) + 1
        for k,v in countArr.items():
            if v%2 == 1:
                return k