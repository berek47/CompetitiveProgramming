 queue = deque([root])
        current_level_nodes = []
        depth = 1
        
        while queue:
            level_node_count = len(queue)
            is_odd_level = (depth % 2 == 0)
            
            for _ in range(level_node_count):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                if is_odd_level:
                    current_level_nodes.append(node)
            
            if is_odd_level:
                for i in range(len(current_level_nodes) // 2):
                    current_level_nodes[i].val, current_level_nodes[-i-1].val = current_level_nodes[-i-1].val, current_level_nodes[i].val
                current_level_nodes = []
            
            depth += 1
        
        return root
