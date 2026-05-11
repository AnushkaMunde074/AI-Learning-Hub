#!/usr/bin/env python3
"""
Breadth-First Search (BFS) Implementation
Finds shortest path in unweighted graphs
"""

from collections import deque
from typing import List, Tuple, Optional


class BFS:
    """Breadth-First Search implementation"""
    
    def __init__(self, graph: dict):
        """
        Initialize BFS with graph
        
        Args:
            graph: Dictionary representation of graph
                   Example: {'A': ['B', 'C'], 'B': ['A', 'D']}
        """
        self.graph = graph
        self.visited = set()
        self.queue = deque()
    
    def search(self, start: str, goal: str) -> Optional[List[str]]:
        """
        Find shortest path from start to goal using BFS
        
        Args:
            start: Starting node
            goal: Goal node
            
        Returns:
            List of nodes in shortest path, or None if no path exists
        """
        self.visited.clear()
        self.queue.clear()
        
        # Track parent of each node for path reconstruction
        parent = {start: None}
        self.queue.append(start)
        self.visited.add(start)
        
        while self.queue:
            node = self.queue.popleft()
            
            if node == goal:
                # Reconstruct path
                path = []
                current = goal
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1]
            
            # Explore neighbors
            for neighbor in self.graph.get(node, []):
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    parent[neighbor] = node
                    self.queue.append(neighbor)
        
        return None  # No path found
    
    def search_all_reachable(self, start: str) -> set:
        """
        Find all nodes reachable from start
        
        Args:
            start: Starting node
            
        Returns:
            Set of all reachable nodes
        """
        self.visited.clear()
        self.queue.clear()
        
        self.queue.append(start)
        self.visited.add(start)
        
        while self.queue:
            node = self.queue.popleft()
            
            for neighbor in self.graph.get(node, []):
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    self.queue.append(neighbor)
        
        return self.visited
    
    def shortest_path_distance(self, start: str) -> dict:
        """
        Find shortest distance from start to all reachable nodes
        
        Args:
            start: Starting node
            
        Returns:
            Dictionary with distances from start
        """
        distances = {start: 0}
        self.queue.clear()
        self.queue.append(start)
        
        while self.queue:
            node = self.queue.popleft()
            
            for neighbor in self.graph.get(node, []):
                if neighbor not in distances:
                    distances[neighbor] = distances[node] + 1
                    self.queue.append(neighbor)
        
        return distances


def example_social_network():
    """Example: Finding shortest path in social network"""
    print("=" * 60)
    print("BFS Example: Social Network")
    print("=" * 60)
    
    # Social network graph
    friends = {
        'Alice': ['Bob', 'Charlie'],
        'Bob': ['Alice', 'David', 'Eve'],
        'Charlie': ['Alice', 'Frank'],
        'David': ['Bob', 'Eve'],
        'Eve': ['Bob', 'David', 'Frank'],
        'Frank': ['Charlie', 'Eve', 'George'],
        'George': ['Frank']
    }
    
    bfs = BFS(friends)
    
    # Find shortest connection
    print("\nFinding shortest path between Alice and George...")
    path = bfs.search('Alice', 'George')
    
    if path:
        print(f"Path: {' -> '.join(path)}")
        print(f"Distance: {len(path) - 1} hops")
    else:
        print("No path found")
    
    # Find all reachable friends
    print("\nFinding all people Alice can reach...")
    reachable = bfs.search_all_reachable('Alice')
    print(f"Reachable: {sorted(reachable)}")
    
    # Show distances
    print("\nDistance from Alice to everyone...")
    distances = bfs.shortest_path_distance('Alice')
    for person in sorted(distances.keys()):
        print(f"  {person}: {distances[person]} hops")


def example_maze():
    """Example: Finding path through maze"""
    print("\n" + "=" * 60)
    print("BFS Example: Maze Solving")
    print("=" * 60)
    
    # Maze represented as graph
    # Each position is connected to adjacent valid positions
    maze = {
        'start': ['A', 'B'],
        'A': ['start', 'C'],
        'B': ['start', 'D'],
        'C': ['A', 'goal'],
        'D': ['B', 'goal'],
        'goal': ['C', 'D']
    }
    
    bfs = BFS(maze)
    path = bfs.search('start', 'goal')
    
    print(f"\nMaze path: {' -> '.join(path)}")
    print(f"Steps: {len(path) - 1}")


def main():
    """Run BFS examples"""
    example_social_network()
    example_maze()
    
    # Performance test
    print("\n" + "=" * 60)
    print("Performance Analysis")
    print("=" * 60)
    print("\nBFS Characteristics:")
    print("✓ Complete: Always finds solution if exists")
    print("✓ Optimal: Finds shortest path")
    print("✗ Space: Requires O(b^d) memory")
    print("✗ Time: O(b^d) time complexity")
    print("\nBest for: Unweighted graphs, shortest path needed")


if __name__ == "__main__":
    main()
