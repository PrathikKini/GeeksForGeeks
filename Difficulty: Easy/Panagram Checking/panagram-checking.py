#User function Template for python3

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        panagram = set()
        for char in s.lower():
            if 'a' <= char <= 'z':
                panagram.add(char)
        return len(panagram) == 26