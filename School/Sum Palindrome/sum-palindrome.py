#User function Template for python3

class Solution:
    def palindrome(self,num):
        return str(num) == str(num)[::-1]
    def isSumPalindrome (self, n):
        if self.palindrome(n):
            return n
        # code here 
        for _ in range(5):
            rev_num = int(str(n)[::-1])
            n += rev_num
            if self.palindrome(n):
                return n
        return -1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isSumPalindrome(n))
# } Driver Code Ends