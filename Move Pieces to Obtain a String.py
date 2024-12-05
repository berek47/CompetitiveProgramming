class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_positions = [(char, i) for i, char in enumerate(start) if char != "_"]
        target_positions = [(char, i) for i, char in enumerate(target) if char != "_"]
        if len(start_positions) != len(target_positions):
            return False
        for (start_char, start_index), (target_char, target_index) in zip(start_positions, target_positions):
            if start_char != target_char or (start_char == "L" and start_index < target_index) or (start_char == "R" and start_index > target_index):
                return False
        return True
