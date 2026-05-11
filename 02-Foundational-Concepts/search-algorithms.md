# Search Algorithms - Comprehensive Guide

## Overview

Search algorithms are fundamental to AI problem-solving. They find solutions in state spaces by exploring possible states.

## Problem Representation

### Components

1. **Initial State**: Starting configuration
2. **Goal State**: Desired outcome
3. **Actions**: Possible moves from each state
4. **Transition Model**: Result of taking action
5. **Path Cost**: Cost of each step

### Example: 8-Puzzle
```
Initial:    Goal:
1 2 3       1 2 3
4 5 6   ->  4 5 6
7 8 .       7 8 .

Actions: Move tile up/down/left/right
```

## Uninformed Search (Blind Search)

No heuristic information used.

### 1. Breadth-First Search (BFS)

**Strategy**: Explore level by level

**Algorithm**:
```
1. Create queue with initial state
2. While queue not empty:
   - Dequeue state
   - If goal: return solution
   - Enqueue all children
```

**Properties**:
- ✅ Complete: Always finds solution if it exists
- ✅ Optimal: Finds shortest path
- ❌ Time: O(b^d) where b=branching factor, d=depth
- ❌ Space: O(b^d) - memory intensive

**Use when**: 
- Solution depth unknown
- All path costs equal
- Need guaranteed shortest path

### 2. Depth-First Search (DFS)

**Strategy**: Go deep before backtracking

**Algorithm**:
```
1. Create stack with initial state
2. While stack not empty:
   - Pop state
   - If goal: return solution
   - Push all children
```

**Properties**:
- ❌ Complete: Can get stuck in infinite loops
- ❌ Optimal: Doesn't find shortest path
- ✅ Time: O(b^m) where m=max depth
- ✅ Space: O(bm) - more memory efficient

**Use when**:
- Memory limited
- Solution likely at deeper levels
- Need to explore all possibilities

### 3. Uniform Cost Search (UCS)

**Strategy**: Expand lowest-cost nodes first

**Algorithm**:
```
1. Create priority queue (sorted by cost)
2. While queue not empty:
   - Dequeue lowest-cost state
   - If goal: return solution
   - Enqueue all children with updated costs
```

**Properties**:
- ✅ Complete: Yes
- ✅ Optimal: Yes
- Time: O(b^(1+floor(C*/e)))
- Space: Similar to BFS

**Use when**:
- Different path costs matter
- Need optimal solution
- Like Dijkstra's algorithm

## Informed Search (Heuristic Search)

Uses problem-specific knowledge.

### Heuristic Function

**Definition**: h(n) = estimated cost from node n to goal

**Properties**:
- **Admissible**: h(n) ≤ actual cost (never overestimates)
- **Consistent**: h(n) ≤ cost(n→n') + h(n')
- **More informed**: h(n) closer to actual cost = better

**Good heuristics**:
- Manhattan distance for grid problems
- Straight-line distance for pathfinding
- Relaxed problem solutions

### 1. Greedy Best-First Search

**Strategy**: Expand node closest to goal

**Algorithm**:
```
1. Create priority queue (sorted by h)
2. While queue not empty:
   - Dequeue node with lowest h(n)
   - If goal: return solution
   - Enqueue all children
```

**Properties**:
- ❌ Complete: No
- ❌ Optimal: No
- ✅ Time: O(bm)
- ✅ Space: O(bm)

**Use when**:
- Memory limited
- Heuristic very good
- Don't need optimal solution

### 2. A* Search

**Strategy**: Expand node with lowest f(n) = g(n) + h(n)

Where:
- g(n) = actual cost from start to n
- h(n) = estimated cost from n to goal
- f(n) = total estimated cost

**Algorithm**:
```
1. Create priority queue (sorted by f)
2. While queue not empty:
   - Dequeue node with lowest f(n)
   - If goal: return solution
   - Enqueue all children with updated f values
```

**Properties**:
- ✅ Complete: Yes (if graph finite)
- ✅ Optimal: Yes (if heuristic admissible)
- Time: O(b^d)
- Space: O(b^d)

**Advantages**:
- Optimal and complete
- Efficient with good heuristic
- Balanced between actual and estimated cost

**Use when**:
- Need optimal solution
- Have good heuristic
- Memory available

## Adversarial Search (Game Playing)

### Minimax Algorithm

**Concept**: Assume opponent plays optimally

**Algorithm**:
```
if terminal state:
    return value
    
if maximizing player:
    return max(minimax(child) for all children)
else:
    return min(minimax(child) for all children)
```

**Properties**:
- Complete and optimal (with perfect play)
- Time: O(b^d)
- Space: O(bd)

### Alpha-Beta Pruning

**Optimization**: Cut branches that can't affect result

```
Alpha = best value for maximizer
Beta = best value for minimizer

if value >= beta:
    prune (beta cutoff)
if value > alpha:
    alpha = value
```

**Improvement**: Up to O(b^(d/2)) in best case

## Comparison Table

| Algorithm | Complete | Optimal | Time | Space | Use Case |
|-----------|----------|---------|------|-------|----------|
| BFS | ✅ | ✅ | O(b^d) | O(b^d) | Shortest path |
| DFS | ❌ | ❌ | O(b^m) | O(bm) | Memory limited |
| UCS | ✅ | ✅ | O(b^(1+C*/e)) | High | Variable costs |
| Greedy | ❌ | ❌ | O(bm) | O(bm) | Fast estimate |
| A* | ✅ | ✅ | O(b^d) | O(b^d) | Optimal + efficient |

## Practical Recommendations

**Choose based on:**

1. **Need optimal solution?**
   - Yes → A* (with good heuristic) or UCS
   - No → Greedy or DFS

2. **Memory available?**
   - Limited → DFS or Iterative Deepening
   - Enough → BFS or A*

3. **Path costs important?**
   - Yes → UCS or A*
   - No → BFS or DFS

4. **Have good heuristic?**
   - Yes → A*
   - No → UCS or BFS

---

Next: Implement these algorithms in Python!
