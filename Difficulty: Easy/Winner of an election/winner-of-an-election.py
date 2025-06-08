#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        freq = {}
        for i in arr:
            freq[i] = freq.get(i,0) + 1
        
        max_val = max(freq.values())
        names = [name for name, count in freq.items() if max_val == count]
        winner =  min(names)
        
        return winner, max_val