class Solution:
    def isLucky(self, n): 
        #code here
        def is_lucky(n,counter = 2):
            if counter > n:
                return 1
            if n % counter == 0:
                return 0
            n -= (n//counter)
            return is_lucky(n,counter+1)
        return is_lucky(n)