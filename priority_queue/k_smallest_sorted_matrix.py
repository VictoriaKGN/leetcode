# 378. Kth Smallest Element in a Sorted Matrix

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [] # (val, (r, c))

        for r in range(min(k, n)):
            heapq.heappush(heap, (matrix[r][0], (r, 0)))

        val = 0
        for i in range(k):
            val, (r, c) = heapq.heappop(heap)
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], (r, c + 1)))

        return val
