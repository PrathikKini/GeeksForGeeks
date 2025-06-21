class Solution:
    def areIsomorphic(self,s1,s2):
        # code here 
        d1 = {}
        d2 = {}
        for i in range(len(s1)):
            d1[s1[i]] = d1.get(s1[i],0)+1
            d2[s2[i]] = d2.get(s2[i],0)+1
        return True if list(d1.values()) == list(d2.values()) else False