# TLE code
# fill the lower the wall


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        queue = []
        res = 0
        for i,h in enumerate(height):
            # print("-"*10)
            # print(h, queue)
            if len(queue) == 0 and h == 0:
                continue
            if len(queue) == 0 or h < queue[-1]:
                # print("append")
                queue.append(h)
            else:
                i = 0
                left = queue[0] if queue[0] < h else h
                # print("left", left)
                while i < len(queue):
                    if queue[i] < h:
                        x = queue.pop(i)
                        queue.append(h)
                        # print("add", x)
                        res += (left-x)
                    else:
                        i += 1
                queue.append(h)
        return res
