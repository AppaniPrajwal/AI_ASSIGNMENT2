from collections import deque


directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

def bfs_shortest_path(grid):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)

  
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

   
    queue = deque([(0, 0, [(0, 0)])])
    visited = set([(0, 0)])

    while queue:
        x, y, path = queue.popleft()

        if (x, y) == goal:
            return len(path), path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, path + [(nx, ny)]))

    return -1, [] 

if __name__ == "__main__":
    grid = [
        [0, 1, 0],
        [0, 0, 0],
        [1, 0, 0]
    ]
    length, path = bfs_shortest_path(grid)
    print("Shortest path length:", length)
    print("Path:", path)
