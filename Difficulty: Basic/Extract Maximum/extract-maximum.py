#User function Template for python3

class Solution:
    def extractMaximum(self,S): 
        # code here
        max_num = -1
        current_num = ""
        
        for char in S:
            if char.isdigit():
                current_num+=char
            else:
                if current_num:
                    max_num = max(max_num,int(current_num))
                    current_num = ""
        
        if current_num:
            max_num = max(max_num,int(current_num))
        return max_num
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        print(ob.extractMaximum(S)) 

        print("~")
# } Driver Code Ends