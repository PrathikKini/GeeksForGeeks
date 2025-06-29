 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        numset = set(arr)
        longest = 0
        
        for num in numset:
            if (num - 1) not in numset:
                length = 1
                while (num+length) in numset:
                    length += 1
                longest = max(length,longest)
        return longest