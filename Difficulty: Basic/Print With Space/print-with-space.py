#User function Template for python3
def utility():
    a = input()
    b = input()

    #Write your code below that prints a <space> b
    print(a, b)



#{ 
 # Driver Code Starts
def main():
    t = int(input())
    while (t > 0):
        utility()
        t -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends