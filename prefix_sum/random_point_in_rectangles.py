import random

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        
        self.rects = rects
        self.areas = [0] * len(rects)
        
        for i in range(len(rects)):
            self.areas[i] = (rects[i][2] - rects[i][0] + 1) * (rects[i][3] - rects[i][1] + 1)
        
        total_area = sum(self.areas)

        for i in range(len(rects)):
            self.areas[i] = self.areas[i] / total_area
        

    def pick(self):
        """
        :rtype: List[int]
        """
        rect = random.choices(population=self.rects, weights=self.areas, k=1)[0]
        return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]      


# Your Solution object will be instantiated and called as such:
obj = Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])
param_1 = obj.pick()