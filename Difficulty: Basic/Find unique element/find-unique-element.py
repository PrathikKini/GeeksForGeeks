class Solution:
    def find_unique(self, k, arr):
        #code here
        freq = {}
        for i in arr:
            freq[i] = 1 + freq.get(i,0)
        for key,val in freq.items():
            if val!=k:
                return key


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())
    for _ in range(t):
        k = int(input().strip())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        print(solution.find_unique(k, arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends