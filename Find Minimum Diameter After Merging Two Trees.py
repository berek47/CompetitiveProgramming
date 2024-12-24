class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = {i: set() for i in range(n)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        seen = [0] * n
        def dfs(node):
            if seen[node]:
                return []
            seen[node] = 1
            longest_path = []
            for neighbor in graph[node]:
                if not seen[neighbor]:
                    path_from_neighbor = dfs(neighbor)
                    if len(path_from_neighbor) > len(longest_path):
                        longest_path = path_from_neighbor
            longest_path.append(node)
            seen[node] = 0
            return longest_path
        
        farthest_node = dfs(0)[0]
        longest_path = dfs(farthest_node)
        return max(len(longest_path) - 1, 0)
    
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        diameter1 = self.treeDiameter(edges1)
        diameter2 = self.treeDiameter(edges2)
        combined_diameter = (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1
        return max(diameter1, diameter2, combined_diameter)
