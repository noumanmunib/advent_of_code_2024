import heapq

def parse_input(file_path):
    """Reads the input file and returns a list of tuples representing corrupted coordinates."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [tuple(map(int, line.strip().split(','))) for line in lines]

def simulate_memory_corruption(corrupted_coords, grid_size):
    """Simulates the corruption on the grid."""
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    return grid

def is_valid(x, y, grid):
    """Checks if the coordinate (x, y) is valid and not corrupted."""
    return 0 <= x < len(grid) and 0 <= y < len(grid) and grid[y][x] == 0

def shortest_path(grid):
    """Finds the shortest path from top-left to bottom-right using A* algorithm."""
    start = (0, 0)
    end = (len(grid) - 1, len(grid) - 1)
    
    if grid[start[1]][start[0]] == 1 or grid[end[1]][end[0]] == 1:
        return -1  # No path if start or end is corrupted

    # Priority queue: (cost, x, y)
    pq = [(0, start[0], start[1])]
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Left, Right, Up, Down

    while pq:
        cost, x, y = heapq.heappop(pq)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Check if we reached the end
        if (x, y) == end:
            return cost

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid) and (nx, ny) not in visited:
                heapq.heappush(pq, (cost + 1, nx, ny))

    return -1  # No path found

def find_blocking_byte(corrupted_coords, grid_size):
    """Finds the first byte that prevents the exit from being reachable."""
    grid = simulate_memory_corruption([], grid_size)

    for idx, (x, y) in enumerate(corrupted_coords):
        grid[y][x] = 1  # Add corruption
        if shortest_path(grid) == -1:
            return x, y  # Return the first blocking byte

def main():
    file_path = "E:/Advent of Code 2024/Day 18/input.txt"
    grid_size = 71  # Memory space dimensions (0 to 70 inclusive)
    corrupted_coords = parse_input(file_path)

    # Find the first blocking byte
    blocking_byte = find_blocking_byte(corrupted_coords, grid_size)
    print(f"The coordinates of the first byte that prevents the exit are: {blocking_byte[0]},{blocking_byte[1]}")

if __name__ == "__main__":
    main()