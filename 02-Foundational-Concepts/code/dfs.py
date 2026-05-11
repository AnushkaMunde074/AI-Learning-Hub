#!/usr/bin/env python3
"""
Depth-First Search (DFS) Implementation
Explores deeply before backtracking
"""

from typing import List, Optional, Callable


class DFS:
    """Depth-First Search implementation"""
    
    def __init__(self, graph: dict):
        """
        Initialize DFS with graph
        
        Args:
            graph: Dictionary representation of graph
        """
        self.graph = graph
        self.visited = set()
    
    def search_recursive(self, node: str, goal: str, 
                        path: Optional[List[str]] = None) -> Optional[List[str]]:
        """
        DFS using recursion
        
        Args:
            node: Current node
            goal: Goal node
            path: Current path (internal use)
            
        Returns:
            Path to goal or None
        """
        if path is None:
            path = []
            self.visited.clear()
        
        path.append(node)
        self.visited.add(node)
        
        if node == goal:
            return path
        
        for neighbor in self.graph.get(node, []):
            if neighbor not in self.visited:
                result = self.search_recursive(neighbor, goal, path)
                if result:
                    return result
        
        path.pop()
        return None
    
    def search_iterative(self, start: str, goal: str) -> Optional[List[str]]:
        """
        DFS using stack (iterative approach)
        
        Args:
            start: Starting node
            goal: Goal node
            
        Returns:
            Path to goal or None
        """
        self.visited.clear()
        stack = [(start, [start])]
        
        while stack:
            node, path = stack.pop()
            
            if node in self.visited:
                continue
            
            self.visited.add(node)
            
            if node == goal:
                return path
            
            # Add neighbors to stack (reverse order for consistent order)
            for neighbor in reversed(self.graph.get(node, [])):
                if neighbor not in self.visited:
                    stack.append((neighbor, path + [neighbor]))
        
        return None
    
    def find_all_paths(self, start: str, goal: str) -> List[List[str]]:
        """
        Find all paths from start to goal
        
        Args:
            start: Starting node
            goal: Goal node
            
        Returns:
            List of all paths
        """
        self.visited.clear()
        paths = []
        
        def dfs_all(node, goal, path):
            if node == goal:
                paths.append(path + [node])
                return
            
            for neighbor in self.graph.get(node, []):
                if neighbor not in path:  # Avoid cycles
                    dfs_all(neighbor, goal, path + [node])
        
        dfs_all(start, goal, [])
        return paths
    
    def topological_sort(self) -> Optional[List[str]]:
        """
        Topological sort using DFS (for DAGs)
        
        Returns:
            Topologically sorted nodes
        """
        self.visited.clear()
        stack = []
        
        def dfs_topo(node):
            self.visited.add(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in self.visited:
                    dfs_topo(neighbor)
            stack.append(node)
        
        # Visit all nodes
        for node in self.graph:
            if node not in self.visited:
                dfs_topo(node)
        
        return stack[::-1]
    
    def detect_cycle(self) -> bool:
        """
        Detect if graph has cycle
        
        Returns:
            True if cycle exists
        """
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {node: WHITE for node in self.graph}
        
        def has_cycle_dfs(node):
            color[node] = GRAY
            for neighbor in self.graph.get(node, []):
                if color[neighbor] == GRAY:
                    return True  # Back edge = cycle
                if color[neighbor] == WHITE:
                    if has_cycle_dfs(neighbor):
                        return True
            color[node] = BLACK
            return False
        
        for node in self.graph:
            if color[node] == WHITE:
                if has_cycle_dfs(node):
                    return True
        
        return False


def example_maze_exploration():
    """Example: Exploring maze with DFS"""
    print("=" * 60)
    print("DFS Example: Maze Exploration")
    print("=" * 60)
    
    maze = {
        'start': ['A', 'B'],
        'A': ['start', 'C', 'D'],
        'B': ['start', 'E'],
        'C': ['A', 'goal'],
        'D': ['A', 'F'],
        'E': ['B', 'goal'],
        'F': ['D'],
        'goal': ['C', 'E']
    }
    
    dfs = DFS(maze)
    
    print("\nRecursive DFS:")
    path = dfs.search_recursive('start', 'goal')
    print(f"Path found: {' -> '.join(path) if path else 'None'}")
    
    print("\nIterative DFS:")
    path = dfs.search_iterative('start', 'goal')
    print(f"Path found: {' -> '.join(path) if path else 'None'}")
    
    print("\nAll possible paths:")
    all_paths = dfs.find_all_paths('start', 'goal')
    for i, path in enumerate(all_paths, 1):
        print(f"  Path {i}: {' -> '.join(path)}")


def example_task_dependencies():
    """Example: Task scheduling with topological sort"""
    print("\n" + "=" * 60)
    print("DFS Example: Task Scheduling (Topological Sort)")
    print("=" * 60)
    
    # Tasks with dependencies (directed graph)
    tasks = {
        'main': ['design', 'code'],
        'design': ['requirement'],
        'code': ['design', 'test'],
        'test': ['code'],
        'requirement': [],
        'deploy': ['test']
    }
    
    dfs = DFS(tasks)
    topo_order = dfs.topological_sort()
    
    print("\nTask execution order:")
    for i, task in enumerate(topo_order, 1):
        print(f"  {i}. {task}")


def example_cycle_detection():
    """Example: Detecting cycles in graphs"""
    print("\n" + "=" * 60)
    print("DFS Example: Cycle Detection")
    print("=" * 60)
    
    # Graph without cycle
    graph1 = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    
    dfs1 = DFS(graph1)
    print(f"\nGraph 1 has cycle: {dfs1.detect_cycle()}")
    
    # Graph with cycle
    graph2 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    
    dfs2 = DFS(graph2)
    print(f"Graph 2 has cycle: {dfs2.detect_cycle()}")


def main():
    """Run DFS examples"""
    example_maze_exploration()
    example_task_dependencies()
    example_cycle_detection()
    
    print("\n" + "=" * 60)
    print("DFS Characteristics")
    print("=" * 60)
    print("✓ Memory: O(bm) - more efficient than BFS")
    print("✓ Useful for: Topological sort, cycle detection")
    print("✗ Path: Doesn't guarantee shortest path")
    print("✗ Complete: May not find solution in infinite graphs")


if __name__ == "__main__":
    main()
