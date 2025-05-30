#User function Template for python3

"""
input - 
s - given string 

output - 
return 0 if not panagram else return 1
"""
class Solution:
    def isPanagram(self,s):
        #your code here
        S = s.lower()
        set_s = set()
        for char in S:
            if char.isalpha():
                set_s.add(char)
        return 1 if len(set_s) == 26 else 0