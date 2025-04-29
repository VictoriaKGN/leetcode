# 621. Task Scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        time = 0
        queue = deque() # [(-val, time)]

        while heap or queue:
            time += 1

            if heap:
                val = heapq.heappop(heap)
                if val + 1 < 0:
                    queue.append((val + 1, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time