class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        total_subarrays = 0
        current_sum = 0
        expected_sum = 0
        
        for i in range(len(arr)):
            current_sum += arr[i]
            expected_sum += i
            
            if current_sum == expected_sum:
                total_subarrays += 1
        
        return total_subarrays
