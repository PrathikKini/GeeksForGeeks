#User function Template for python3
class Solution:
    def merge(self, S1, S2):
        # code here
        i = j = 0
        merged = []
        
        len1, len2 = len(S1), len(S2)
        
        while i < len1 and j < len2:
            merged.append(S1[i])
            merged.append(S2[j])
            i +=1
            j +=1
            
        merged.append(S1[i:])
        merged.append(S2[j:])
        
        return "".join(merged)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1,S2 = map(str,input().strip().split())
        ob = Solution()
        print(ob.merge(S1, S2))
        print("~")
# } Driver Code Ends