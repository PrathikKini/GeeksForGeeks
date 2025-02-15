#User function Template for python3

class Solution:

    def isPossible(self, S):

        # code here
        freq = {}
        for char in S:
            if char in freq:
                freq[char]+=1
            else:
                freq[char] = 1
                
        odd_count = sum(1 for count in freq.values() if count % 2 == 1)
        
        return 1 if odd_count <=1 else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        if solObj.isPossible(S):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends