# 264. Ugly Number II
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [2, 3, 5]
        heap = [1]
        heapq.heapify(heap)
        seen = set()
        popped = None

        for _ in range(n):
            popped = heapq.heappop(heap)

            for num in ugly:
                new_num = popped * num
                if new_num not in seen:
                    seen.add(new_num)
                    heapq.heappush(heap, new_num)
        
        return popped
    
solution = Solution()
solution.nthUglyNumber(10)