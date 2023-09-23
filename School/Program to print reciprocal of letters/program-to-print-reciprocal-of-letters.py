#User function Template for python3
class Solution:
    def reciprocalString(self, S):
        # code here
        res = ""
        for x in S:
            if x>='A' and x<='Z':
                res+=chr(90-(ord(x)-65))
            elif x>='a' and x<='z':
                res+=chr(122-(ord(x)-97))
            else:
                res+=x
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.reciprocalString(S))
# } Driver Code Ends