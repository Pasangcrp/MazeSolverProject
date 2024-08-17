
#* BEST FIRST SEARCH FIRST (heuristic search algorithm)
import heapq

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def best_f_s(maze, start, goal):
    # Priority queue initialized with the start node
    pq = [(manhattan_distance(start, goal), start)]
    # Track visited nodes to prevent reprocessing
    visited = set()
    # Track the path for reconstructing the final solution
    came_from = {start: None}

    while pq:
        # Pop the node with the smallest heuristic value (closest to the goal)
        _, current = heapq.heappop(pq)

        if current == goal:
            # Reconstruct the path by backtracking from goal to start
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1] 
        visited.add(current)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            # Ensure the neighbor is within the maze bounds and is not a wall ('1')
            if (0 <= neighbor[0] < len(maze) and
                0 <= neighbor[1] < len(maze[0]) and
                maze[neighbor[0]][neighbor[1]] == '0' and
                neighbor not in visited):

                # Push the neighbor to the priority queue with its heuristic value
                heapq.heappush(pq, (manhattan_distance(neighbor, goal), neighbor))
                came_from[neighbor] = current

    return None  
