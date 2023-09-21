#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        S = list(s)
        left , right = 0, len(S)-1
        vowels = "aeiou"
        
        while left < right:
            while left<right and S[left] not in vowels:
                left+=1
            while left<right and S[right] not in vowels:
                right-=1
            S[left], S[right] = S[right], S[left]
            left+=1
            right-=1
        return "".join(S)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends