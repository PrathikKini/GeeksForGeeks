
class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        return len([i for i in range(1,n+1) if '4' in str(i)])
            
