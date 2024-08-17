
#* DEPTH-FIRST SEARCH (Non-Heuristic Search Algorithm)
def dfs(maze, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return path

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbor = (start[0] + dx, start[1] + dy)
        if (0 <= neighbor[0] < len(maze) and
            0 <= neighbor[1] < len(maze[0]) and
            maze[neighbor[0]][neighbor[1]] == '0' and
            neighbor not in visited):
            
            result = dfs(maze, neighbor, goal, visited, path)
            if result:
                return result

    path.pop()
    return None

