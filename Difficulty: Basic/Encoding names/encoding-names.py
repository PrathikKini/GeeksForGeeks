#User function Template for python3

class Solution:
    def encodeTheName(self, S):
        # code here 
        encode = ""
        for i in range(len(S)):
            encode+=str(ord(S[i])-10+i)
        return encode