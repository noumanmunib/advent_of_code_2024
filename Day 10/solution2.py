def read_input(file_path):
    """Reads the input file and returns the topographic map as a list of lists."""
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

def find_trailheads(topographic_map):
    """Find all trailhead positions in the map (positions with height 0)."""
    trailheads = []
    for i in range(len(topographic_map)):
        for j in range(len(topographic_map[0])):
            if topographic_map[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def dfs_count_trails(map_, x, y, height, visited):
    """Recursive DFS to count distinct hiking trails."""
    # Check bounds
    if x < 0 or x >= len(map_) or y < 0 or y >= len(map_[0]):
        return 0
    
    # Check if the current position is invalid
    if map_[x][y] != height or visited[x][y]:
        return 0

    # Mark current position as visited for this trail
    visited[x][y] = True

    # If the current height is 9, we've reached a valid endpoint
    if height == 9:
        visited[x][y] = False  # Unmark for other trails
        return 1

    # Continue exploring neighbors
    total_trails = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        total_trails += dfs_count_trails(map_, x + dx, y + dy, height + 1, visited)

    # Unmark the current position for other trails
    visited[x][y] = False
    return total_trails

def calculate_total_ratings(map_):
    """Calculate the total rating of all trailheads."""
    trailheads = find_trailheads(map_)
    total_rating = 0

    for trailhead in trailheads:
        visited = [[False for _ in range(len(map_[0]))] for _ in range(len(map_))]
        rating = dfs_count_trails(map_, trailhead[0], trailhead[1], 0, visited)
        total_rating += rating

    return total_rating

def main():
    fn = "E:/Advent of Code 2024/Day 10/input.txt"
    topographic_map = read_input(fn)
    total_rating = calculate_total_ratings(topographic_map)
    print(f"Total rating of all trailheads: {total_rating}")

if __name__ == "__main__":
    main()