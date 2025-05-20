
#User function Template for python3
from collections import OrderedDict
class Solution:
    
    #Function to find repeated character whose first appearance is leftmost.
    def repeatingCharacter(self,s):
        #code here
        char_set = OrderedDict()
        for char in s:
            char_set[char] = 1 + char_set.get(char,0)
        for key,val in char_set.items():
            if val > 1:
                return s.index(key)
        return -1