class Solution:
    def leaders(self, arr):
        # code here
        result = []
        max_arr_num = float('-inf')
        
        for num in reversed(arr):
            if num>=max_arr_num:
                result.append(num)
                max_arr_num = num
        return result[::-1]
            

#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends