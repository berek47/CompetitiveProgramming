class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_counts = {}
        for row in matrix:
            base_pattern = tuple(row)
            flipped_pattern = tuple(1 - x for x in row)
            canonical_pattern = min(base_pattern, flipped_pattern)
            if canonical_pattern not in pattern_counts:
                pattern_counts[canonical_pattern] = 0
            pattern_counts[canonical_pattern] += 1
        return max(pattern_counts.values())
