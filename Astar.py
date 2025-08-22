
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)

  
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

   
    frontier = [(start, [start], 0)]
    visited = {}

    while frontier:
      
        frontier.sort(key=lambda x: x[2] + heuristic(x[0], goal))
        (x, y), path, g = frontier.pop(0)

        
        if (x, y) in visited and visited[(x, y)] <= g:
            continue
        visited[(x, y)] = g

        
        if (x, y) == goal:
            return len(path), path

        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                frontier.append(((nx, ny), path + [(nx, ny)], g + 1))

    return -1, []


if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    length, path = a_star_search(grid)
    if length == -1:
        print("No path exists")
    else:
        print("Shortest Path Length:", length)
        print("Path:", path)