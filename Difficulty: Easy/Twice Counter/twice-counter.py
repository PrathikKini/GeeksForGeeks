#User function Template for python3

class Solution:
    def countWords(self,List, n):
        #code here
        countA = {}
        for i in range(len(List)):
            countA[List[i]] = countA.get(List[i],0) + 1
        return sum([1 for k,v in countA.items() if v == 2])