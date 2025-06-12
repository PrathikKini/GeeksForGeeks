class Solution:
    def ExtractNumber(self,sentence):
        #code here
        word_lst = sentence.split()
        l = []
        for word in word_lst:
            if word.isdigit() and '9' not in word:
                l.append(word)
        return max(list(map(int,l))) if l else -1