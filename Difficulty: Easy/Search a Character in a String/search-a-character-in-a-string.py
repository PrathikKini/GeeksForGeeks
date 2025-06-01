#User function Template for python3
class Solution:
    
    # Function to search for a character in the string
    def searchCharacter(self, s, ch):
        # code here
        for i,n in enumerate(s,0):
            if ch == n:
                return i
        return -1