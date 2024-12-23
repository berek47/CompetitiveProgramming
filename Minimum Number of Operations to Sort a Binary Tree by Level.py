# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def calculate_minimum_swaps(arr):
            n = len(arr)
            swaps = 0
            temp = arr.copy()
            index_map = {}

            for i in range(n):
                index_map[arr[i]] = i

            temp.sort()

            for i in range(n):
                if arr[i] != temp[i]:
                    swaps += 1
                    original_value = arr[i]
                    arr[i], arr[index_map[temp[i]]] = arr[index_map[temp[i]]], arr[i]
                    index_map[original_value] = index_map[temp[i]]
                    index_map[temp[i]] = i

            return swaps

        total_operations = 0
        if not root:
            return 0

        level_queue = [root]

        while level_queue:
            level_size = len(level_queue)
            level_values = []

            for _ in range(level_size):
                node = level_queue.pop(0)
                level_values.append(node.val)

                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)

            total_operations += calculate_minimum_swaps(level_values)

        return total_operations
