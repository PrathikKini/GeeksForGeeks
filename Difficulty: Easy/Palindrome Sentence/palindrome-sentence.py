#User function Template for python3
class Solution:
	def sentencePalindrome(self, s):
		# your code here
		s = s.lower()
	    l, r = 0, len(s)-1
	    while l < r:
	        while l < r and not self.alphanum(s[l]):
	            l+=1
	        while l < r and not self.alphanum(s[r]):
	            r-=1
	        if s[l] != s[r]:
	           return False
	        l,r = l+1, r-1
	    return True
	def alphanum(self,c):
	    return (ord('a')<=ord(c)<=ord('z') or 
	        ord('0')<=ord(c)<=ord('9'))