#User function Template for python3

class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self, s):
        #code here
        freq = [0] * 26
        
        for i in s:
            freq[ord(i)-ord('a')]+=1
            
        result= ''
        max_freq = 0
        
        for i in range(26):
            if freq[i] > max_freq:
                max_freq = freq[i]
                result = chr(i+ord('a'))
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        print(Solution().getMaxOccurringChar(s))
        print("~")

# } Driver Code Ends