# 29. Divide Two Integers
# using the hand divide method
# need to learn how to use & and |

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = False
        if dividend < 0:
            dividend = -dividend
            flag = not flag
        if divisor < 0:
            divisor = -divisor
            flag = not flag
        str_end = str(dividend)
        result = 0
        next_c = 0
        this_dividend = ""
        while next_c < len(str_end):
            this_dividend += str_end[next_c]
            this_number = 0
            temp = divisor
            for i in range(10):
                if temp > int(this_dividend):
                    this_number = i
                    break
                else:
                    temp += divisor
            result = result * 10 + this_number
            head = int(this_dividend) - temp + divisor
            # print("next char:", str_end[next_c], 
            #       "this dividend", this_dividend, 
            #       "this number", this_number,
            #       "head", head)
            next_c += 1
            this_dividend = str(head)
            
        if flag:
            if result > 2**31:
                return -(2**31)
            else:
                return -result
        else:
            if result > 2**31-1:
                return 2**31-1
            else:
                return result
