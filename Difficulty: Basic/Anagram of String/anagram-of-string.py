# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(s1,s2):
    
    #add code here
    
    l = [0] * 26
    
    for i in s1:
        l[ord(i)-97] += 1
    for i in s2:
        l[ord(i)-97] -= 1
    
    return sum(abs(x) for x in l)
    
    


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        str2 = input()
        print(remAnagram(str1, str2))
        print("~")

# } Driver Code Ends