#!/usr/bin/env python3
"""
A* Search Algorithm Implementation
Optimal and complete search with heuristics
"""

import heapq
import math
from typing import List, Tuple, Dict, Optional, Callable


class Node:
    """Represents a node in search space"""
    
    def __init__(self, position: Tuple[int, int], g: float = 0, h: float = 0):
        self.position = position
        self.g = g  # Cost from start
        self.h = h  # Heuristic cost to goal
        self.f = g + h  # Total cost
        self.parent = None
    
    def __lt__(self, other):
        """For priority queue comparison"""
        return self.f < other.f
    
    def __eq__(self, other):
        return self.position == other.position


class AStar:
    """A* search algorithm"""
    
    def __init__(self, start: Tuple[int, int], goal: Tuple[int, int],
                 heuristic: Callable = None):
        self.start = start
        self.goal = goal
        self.heuristic = heuristic or self.manhattan_distance
        self.open_list = []
        self.closed_set = set()
        self.g_score = {}
    
    def manhattan_distance(self, pos: Tuple[int, int]) -> float:
        """
        Manhattan distance heuristic
        Good for grid-based pathfinding
        """
        return abs(pos[0] - self.goal[0]) + abs(pos[1] - self.goal[1])
    
    def euclidean_distance(self, pos: Tuple[int, int]) -> float:
        """
        Euclidean distance heuristic
        Good for continuous spaces
        """
        return math.sqrt((pos[0] - self.goal[0])**2 + (pos[1] - self.goal[1])**2)
    
    def get_neighbors(self, pos: Tuple[int, int], 
                     grid: Optional[List[List[int]]] = None) -> List[Tuple[int, int]]:
        """
        Get valid neighbor positions
        
        Args:
            pos: Current position
            grid: Optional obstacle grid (1 = obstacle)
            
        Returns:
            List of valid neighbor positions
        """
        x, y = pos
        neighbors = []
        
        # 4-directional movement
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # 8-directional (uncomment for diagonal movement)
        # directions = [(0, 1), (1, 1), (1, 0), (1, -1), 
        #              (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check bounds
            if 0 <= nx < 100 and 0 <= ny < 100:  # Grid size
                # Check obstacles
                if grid is None or grid[nx][ny] == 0:
                    neighbors.append((nx, ny))
        
        return neighbors
    
    def search(self, grid: Optional[List[List[int]]] = None) -> Optional[List[Tuple[int, int]]]:
        """
        Perform A* search
        
        Args:
            grid: Optional grid with obstacles
            
        Returns:
            Path from start to goal, or None if no path exists
        """
        start_node = Node(self.start, 0, self.heuristic(self.start))
        heapq.heappush(self.open_list, start_node)
        self.g_score[self.start] = 0
        
        while self.open_list:
            current = heapq.heappop(self.open_list)
            
            if current.position in self.closed_set:
                continue
            
            if current.position == self.goal:
                # Reconstruct path
                path = []
                node = current
                while node:
                    path.append(node.position)
                    node = node.parent
                return path[::-1]
            
            self.closed_set.add(current.position)
            
            for neighbor_pos in self.get_neighbors(current.position, grid):
                if neighbor_pos in self.closed_set:
                    continue
                
                # Calculate tentative g score
                tentative_g = current.g + 1
                
                if neighbor_pos not in self.g_score or tentative_g < self.g_score[neighbor_pos]:
                    # This path is better
                    self.g_score[neighbor_pos] = tentative_g
                    h = self.heuristic(neighbor_pos)
                    neighbor_node = Node(neighbor_pos, tentative_g, h)
                    neighbor_node.parent = current
                    heapq.heappush(self.open_list, neighbor_node)
        
        return None  # No path found


def example_grid_pathfinding():
    """Example: Pathfinding on a grid"""
    print("=" * 60)
    print("A* Example: Grid Pathfinding")
    print("=" * 60)
    
    start = (0, 0)
    goal = (5, 5)
    
    astar = AStar(start, goal)
    path = astar.search()
    
    if path:
        print(f"\nPath found: {path}")
        print(f"Path length: {len(path)}")
        print(f"Path: {' -> '.join(str(p) for p in path)}")
    else:
        print("\nNo path found")


def example_graph_pathfinding():
    """Example: Pathfinding in weighted graph"""
    print("\n" + "=" * 60)
    print("A* Example: Graph Pathfinding")
    print("=" * 60)
    
    # Cities with positions
    positions = {
        'A': (0, 0),
        'B': (2, 0),
        'C': (1, 2),
        'D': (3, 1),
        'E': (4, 3)
    }
    
    class GraphAStar(AStar):
        def __init__(self, start, goal, positions):
            super().__init__(start, goal)
            self.positions = positions
            self.graph = {}
        
        def add_edge(self, u, v):
            if u not in self.graph:
                self.graph[u] = []
            self.graph[u].append(v)
        
        def manhattan_distance(self, pos):
            if isinstance(pos, str):
                pos = self.positions[pos]
            goal_pos = self.positions[self.goal]
            return abs(pos[0] - goal_pos[0]) + abs(pos[1] - goal_pos[1])
    
    # Create graph
    gastar = GraphAStar('A', 'E', positions)
    gastar.add_edge('A', 'B')
    gastar.add_edge('A', 'C')
    gastar.add_edge('B', 'D')
    gastar.add_edge('C', 'D')
    gastar.add_edge('D', 'E')
    
    print("\nGraph structure:")
    for node, neighbors in gastar.graph.items():
        print(f"  {node} -> {neighbors}")
    
    print("\nNote: Full graph A* example would require graph extension")


def main():
    """Run A* examples"""
    example_grid_pathfinding()
    example_graph_pathfinding()
    
    print("\n" + "=" * 60)
    print("A* Characteristics")
    print("=" * 60)
    print("✓ Complete: Always finds solution if exists")
    print("✓ Optimal: Finds best path with admissible heuristic")
    print("✓ Efficient: Uses heuristic to guide search")
    print("✗ Memory: Still requires O(b^d) space")
    print("\nBest for: Pathfinding, puzzle solving with good heuristic")


if __name__ == "__main__":
    main()
