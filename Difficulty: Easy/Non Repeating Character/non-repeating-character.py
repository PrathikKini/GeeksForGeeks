class Solution:
    def nonRepeatingChar(self,s):
        #code here
        from collections import OrderedDict
        
        dict_val = OrderedDict()
        
        for i in range(len(s)):
            dict_val[s[i]] = 1 + dict_val.get(s[i],0)
            
        for k, v in dict_val.items():
            if v == 1:
                return k
        return -1
    
    