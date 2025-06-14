#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        countA = {}
        l = []
        for i in range(len(arr)):
            countA[arr[i]] = countA.get(arr[i],0) + 1
        
        for k, v in countA.items():
            if v == 2:
                l.append(k)
        
        for i in range(1,len(arr)+1):
            if i not in countA:
                l.append(i)
                
        return l
