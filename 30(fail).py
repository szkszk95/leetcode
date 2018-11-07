# did not consider the ["aa", "aa", "aa"] ("aaaaaaa") situation

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        temp =[]
        if len(words) == 0 or len(s) == 0:
            return []
        
        l = len(words[0])
        res = []
        i = 0
        while i < len(s):
            # print("-"*10)
            # print(s[i:i+l])
            # print(temp)
            if s[i:i+l] not in words:
                temp = []
                i += 1
                continue
            else:
                temp.append(s[i:i+l])
                if self.if_sub_list(temp, words.copy()) == False:
                    for j in range(len(temp)):
                        if temp[j] == s[i:i+l]:
                            break
                    temp = temp[j+1:]
                    i += l 
                else:
                    i += l
                    if len(temp) == len(words):
                        res.append(i-len(words)*l)
                        temp.pop(0)
                    if i > len(s):
                        break
        return res
    
    def if_sub_list(self, l1, l2):
        for e in l1:
            if e in l2:
                l2.remove(e)
            else:
                return False
        return True
        
