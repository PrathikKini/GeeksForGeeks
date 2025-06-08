#User function Template for python3


class Solution:

    def digitalRoot(self, n):
        '''
        :param n: given number 
        :return: digital root as defined
        '''
        # code here
        return 1 + (n-1) % 9
