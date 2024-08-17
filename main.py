import astar
import breadth_f_s
import depth_f_s
import uniform_c_s
import best_f_s

def print_maze(maze, path=None):
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if path and (i, j) in path:
                print("#", end=" ")  
            else:
                print(col, end=" ")
        print()
    print()

def main():
    maze = [
        ['1', '1', '1', '1', '1', '1'],
        ['1', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '1', '0', '1'],
        ['1', '0', '1', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '1'],
        ['1', '0', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1', '1'],
    ]
    start = (1, 1)
    goal = (5, 4)

    print("Welcome to the Maze Solver!")
    print("Choose an algorithm:")
    print("1. Depth-First Search (DFS)")
    print("2. Breadth-First Search (BFS)")
    print("3. Uniform Cost Search (UCS)")
    print("4. A* Search")
    print("5. Best-First Search")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        print("Solving using Depth-First Search...")
        path = depth_f_s.dfs(maze, start, goal)
    elif choice == '2':
        print("Solving using Breadth-First Search...")
        path = breadth_f_s.breadth_fs(maze, start, goal)
    elif choice == '3':
        print("Solving using Uniform Cost Search...")
        path = uniform_c_s.ucs(maze, start, goal)
    elif choice == '4':
        print("Solving using A* Search...")
        path = astar.a_star(maze, start, goal)
    elif choice == '5':
        print("Solving using Best-First Search...")
        path = best_f_s.best_f_s(maze, start, goal)
    else:
        print("Invalid choice! Exiting...")
        return

    if path:
        print("Path found:")
        print_maze(maze, path)
    else:
        print("No path found from start to goal.")

if __name__ == "__main__":
    main()
