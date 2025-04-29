# 451. Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s) # {char: freq}
        heap = []
        res = ""

        for char, freq in freq.items():
            heapq.heappush(heap, (-freq, char))

        while heap:
            freq, char = heapq.heappop(heap)
            res += -freq * char

        return res