# using the dict instead of the list to save words
# using two pointer as a slide window

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        self.words = {}
        for word in words:
            if word not in self.words.keys():
                self.words[word] = 0
            self.words[word] += 1
        temp =[]
        if len(words) == 0 or len(s) == 0:
            return []
        
        self.l = len(words[0])
        res = []
        
        
        head1, head2 = 0, self.l*len(words)
        while head2 <= len(s):
            if self.if_checked(s[head1:head2]):
                res.append(head1)
            head1 += 1
            head2 += 1
        return res
    
    def if_checked(self, subs):
        temp = self.words.copy()
        for i in range(0, len(subs), self.l):
            e = subs[i:i+self.l]
            if e in temp.keys() and temp[e] >0:
                temp[e] -= 1
            else:
                return False
        return True
