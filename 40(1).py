# recursive method

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = sorted(candidates)
        print(self.candidates)
        self.res = []
        self.run([], 0, target)
        return self.res
        
    def run(self, box, pointer, target):
        # print(box, sum(box))
        if sum(box) == target:
            if box not in self.res:
                self.res.append(box)
            return
        
        if sum(box) > target:
            return

        max_ = max(box) if len(box) > 0 else 0
        
        for i in range(pointer, len(self.candidates)):
            if self.candidates[i] >= max_:
                self.run(box+[self.candidates[i]], i+1, target)
