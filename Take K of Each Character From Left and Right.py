class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0] * 3
        n = len(s)
        for c in s:
            count[ord(c) - ord("a")] += 1
        if any(count[i] < k for i in range(3)):
            return -1
        window = [0] * 3
        left, max_window = 0, 0
        for right in range(n):
            window[ord(s[right]) - ord("a")] += 1
            while left <= right and any(count[i] - window[i] < k for i in range(3)):
                window[ord(s[left]) - ord("a")] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
        return n - max_window
