# 506. Relative Ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        res = [0] * len(score)

        for i in range(len(score)):
            heapq.heappush(heap, (-score[i], i))

        for i in range(1, len(score) + 1):
            _, index = heapq.heappop(heap)
            if i == 1:
                res[index] = "Gold Medal"
            elif i == 2:
                res[index] = "Silver Medal"
            elif i == 3:
                res[index] = "Bronze Medal"
            else:
                res[index] = str(i)

        return res