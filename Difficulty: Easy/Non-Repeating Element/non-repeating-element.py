#User function Template for python3

class Solution:
    def firstNonRepeating(self, arr): 
        # Complete the function
        from collections import OrderedDict
        
        char_set = OrderedDict()
        
        for ch in arr:
            char_set[ch] = char_set.get(ch,0) + 1
            
        for k,v in char_set.items():
            if v == 1:
                return k
        return 0