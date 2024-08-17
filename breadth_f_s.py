
#* BREADTH FIRST SEARCH

from collections import deque

def breadth_fs(maze, start, goal):
    # Initialize the queue with the start position
    queue = deque([start])
    # Track visited positions
    visited = set()
    # Track the path (came_from) for reconstructing the final path
    came_from = {start: None}

    # Perform BFS
    while queue:
        current = queue.popleft()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Return the path from start to goal

        visited.add(current)

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Ensure the neighbor is within the bounds of the maze and is not a wall ('1')
            if (0 <= neighbor[0] < len(maze) and
                0 <= neighbor[1] < len(maze[0]) and
                maze[neighbor[0]][neighbor[1]] == '0' and
                neighbor not in visited):

                queue.append(neighbor)
                came_from[neighbor] = current

    return None  
