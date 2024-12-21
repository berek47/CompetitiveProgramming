class Solution:
    def maxKDivisibleComponents(self, node_count, connections, node_values, divisor):
        adjacency_list = defaultdict(list)
        self.divisible_count = 0

        for start, end in connections:
            adjacency_list[start].append(end)
            adjacency_list[end].append(start)

        def traverse_tree(current_node, parent_node):
            subtree_total = node_values[current_node]
            for adjacent_node in adjacency_list[current_node]:
                if adjacent_node != parent_node:
                    subtree_total += traverse_tree(adjacent_node, current_node)
            
            if subtree_total % divisor == 0:
                self.divisible_count += 1
                return 0
            return subtree_total % divisor

        traverse_tree(0, -1)
        return self.divisible_count
