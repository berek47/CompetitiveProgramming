class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        currentSubarraySum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            # strictly increasing
            if nums[i] > nums[i-1]:
                currentSubarraySum += nums[i]
                maxSum = max(maxSum, currentSubarraySum)
            else:
                currentSubarraySum = nums[i]
        return maxSum
