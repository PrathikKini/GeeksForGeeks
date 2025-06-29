class Solution:
    def areAnagrams(self, s1, s2):
       #code here
       countS1 = {}
       countS2 = {}
       if len(s1) != len(s2):
           return False
           
       for i in range(len(s1)):
           countS1[s1[i]] = countS1.get(s1[i],0) + 1
           countS2[s2[i]] = countS2.get(s2[i],0) + 1
       return countS1 == countS2