class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [0] * (n - k + 1)

        for start in range(n - k + 1):
            consecutive_sorted = True
            for i in range(start, start + k - 1):
                if nums[i + 1] != nums[i] + 1:
                    consecutive_sorted = False
                    break
            result[start] = nums[start + k - 1] if consecutive_sorted else -1

        return result
