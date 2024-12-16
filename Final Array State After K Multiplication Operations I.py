class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        ans = [0] * len(nums)
        nums = [[num, i] for i, num in enumerate(nums)]
        heapq.heapify(nums)

        while k > 0:
            minimum = heapq.heappop(nums)
            minimum[0] *= multiplier
            heapq.heappush(nums, minimum)
            k -= 1
            
        for num, index in nums:
            ans[index] = num
        return ans
