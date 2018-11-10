# recursive method

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = candidates
        self.res = []
        self.run([], target)
        return self.res
        
    def run(self, box, target):
        # print(box, sum(box))
        if sum(box) == target:
            self.res.append(box)
            return
        
        if sum(box) > target:
            return
        
        for i in self.candidates:
            if len(box)==0 or i >= max(box):
                self.run(box+[i], target)
            else:
                continue
                
