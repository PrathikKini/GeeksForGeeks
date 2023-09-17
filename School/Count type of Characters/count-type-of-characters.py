#User function Template for python3

class Solution:
    def count (self,s):
        # your code here
        lc = uc = sc = num = 0
        for i in s:
            if i.isupper():
                uc+=1
            elif i.islower():
                lc+=1
            elif i.isdigit():
                num+=1
            else:
                sc+=1
        return (uc,lc,num,sc)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
# Contributed By: Pranay Bansal

# } Driver Code Ends