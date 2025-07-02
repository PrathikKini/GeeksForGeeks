#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        from collections import defaultdict
        res = defaultdict(list)
        for s in arr:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
        return list(res.values())
