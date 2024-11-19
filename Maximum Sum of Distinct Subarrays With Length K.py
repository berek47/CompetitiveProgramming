class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        start = 0
        num_indices = {}

        for end in range(len(nums)):
            last_seen = num_indices.get(nums[end], -1)
            while start <= last_seen or end - start + 1 > k:
                current_sum -= nums[start]
                start += 1
            num_indices[nums[end]] = end
            current_sum += nums[end]
            if end - start + 1 == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum
