class Solution:
    def duplicates(self, arr, n): 
    	# code here
        seen = set()  # To store elements that have been seen before
        duplicates = set()  # To store duplicate elements
        
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        
        result = sorted(list(duplicates))
        return result if result else [-1]
    	
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends