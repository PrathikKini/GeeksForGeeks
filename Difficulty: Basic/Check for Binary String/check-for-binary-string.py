# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        for i in s:
            if i == '0' or i == '1':
                continue
            else:
                return False
        return True
        #test


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if Solution().isBinary(str):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends