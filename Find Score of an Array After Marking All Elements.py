class Solution:
    def findScore(self, nums: List[int]) -> int:
        pq = []
        for i, n in enumerate(nums):
            heapq.heappush(pq, (n, i))
        marked = set()
        s = 0
        while pq:
            n, i = heapq.heappop(pq)
            if i not in marked:
                marked.add(i - 1)
                marked.add(i)
                marked.add(i + 1)
                s += n
        return s
