
#* UNIFORM COST SEARCH

import heapq

def ucs(maze, start, goal):
    pq = [(0, [start], start)]
    visited = set()

    while pq:
        cost, path, node = heapq.heappop(pq)
        
        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return cost, path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (node[0] + dx, node[1] + dy)
            
            if (0 <= neighbor[0] < len(maze) and
                0 <= neighbor[1] < len(maze[0]) and
                maze[neighbor[0]][neighbor[1]] == '0' and
                neighbor not in visited):
                
                heapq.heappush(pq, (cost + 1, path + [neighbor], neighbor))

    return float('infinity'), []

