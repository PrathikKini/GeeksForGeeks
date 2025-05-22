#User function Template for python3
class Solution:
    def areAnagram(ob, S1, S2):
        # code here 
        if len(S1) != len(S2):
            return 0
            
        count1 = {}
        count2 = {}
        
        for i in range(len(S1)):
            count1[S1[i]] = 1 + count1.get(S1[i],0)
            count2[S2[i]] = 1 + count2.get(S2[i],0)
        
        if count1 == count2:
            return 1
        return 0