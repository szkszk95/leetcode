# fail try
# try to give the path of light
# decimal problem (4, 1.003)shoule be (4,1)

class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        flag = False
        self.p = p
        p1 = (0, 0)
        p2 = (p, q)
        res = -1
        while not flag:
            flag, p1, p2, res = self.reflect(p1, p2)
        return res
        
    def reflect(self, p1, p2):
        print(p1, p2)
        if p2==(0, self.p):
            return True, 0, 0 ,2
        if p2==(self.p, self.p):
            return True, 0, 0 ,1
        if p2==(self.p, 0):
            return True, 0, 0 ,0

        
        k = (p2[1]-p1[1])/(p2[0]-p1[0])
        k = -k
        b_ = p2[1]-k*p2[0]
        
        # x=0
        y1 = b_
        y1 = float(round(y1*1000)/1000)
        if p2[0] != 0:
            if y1 == self.p:
                return True, 0, 0 ,2
            if 0 < y1 < self.p:
                return False, p2, (0, y1), -1
        
        # x=p
        y1 = k*self.p + b_
        y1 = float(round(y1*1000)/1000)
        if p2[0] != self.p:
            if y1 == self.p:
                return True, 0, 0 , 1
            if 0 < y1 < self.p:
                return False, p2, (self.p, y1), -1
        
        # y=0
        x1 = -b_/k
        # x1 = Fraction(-b_, k)
        x1 = float(round(x1*1000)/1000)
        if p2[1] != 0:
            if x1 == self.p:
                return True, 0, 0 , 0
            if 0 < x1 < self.p:
                return False, p2, (x1, 0), -1
        
        # y=p
        x1 = (self.p-b_)/k
        # x1 = Fraction(self.p-b_, k)
        x1 = float(round(x1*1000)/1000)
        if p2[1] != self.p:
            if 0 < x1 < self.p:
                return False, p2, (x1, self.p), -1
        
        
        
        
        
