class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 0
        right = max(quantities)
        while left < right:
            middle = (left + right) // 2
            j = 0
            remaining = quantities[j]

            for i in range(n):
                if remaining <= middle:
                    j += 1
                    if j == len(quantities):
                        break
                    remaining = quantities[j]
                else:
                    remaining -= middle

            if j == len(quantities):
                right = middle
            else:
                left = middle + 1
        return left
