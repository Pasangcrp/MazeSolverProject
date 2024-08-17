
#* A* search (Heuristic Search Algorithm)

import heapq

def a_star(maze, start, goal):
    def heuristic(a, b):
        # Manhattan distance
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  

    pq = []
    heapq.heappush(pq, (0, start))
    came_from = {start: None}
    g_costs = {start: 0}

    while pq:
        current_f, current = heapq.heappop(pq)
        
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == '0':
                new_g = g_costs[current] + 1
                if neighbor not in g_costs or new_g < g_costs[neighbor]:
                    g_costs[neighbor] = new_g
                    f = new_g + heuristic(neighbor, goal)
                    came_from[neighbor] = current
                    heapq.heappush(pq, (f, neighbor))

    return None
