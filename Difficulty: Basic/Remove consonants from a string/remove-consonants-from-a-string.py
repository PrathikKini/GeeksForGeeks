#User function Template for python3

class Solution:
    def removeConsonants(self, s):
        #complete the function here
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        result = [i for i in s if i in vowels]
        return "".join(result) if result else "No Vowel" 
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.removeConsonants(s))
        print("~")
# } Driver Code Ends