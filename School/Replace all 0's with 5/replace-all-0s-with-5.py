#function should return an integer
#your task is to compplete this function
class Solution:
    def convertFive(self,n):
        #Code here
        str_num = str(n)
        str_num = str_num.replace('0','5')
        return int(str_num)


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        print(Solution().convertFive(n))
# Contributed by: Harshit sidhwa

# } Driver Code Ends