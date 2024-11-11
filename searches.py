from collections import deque

class Puzzle:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != 'X'

    def get_neighbors(self, x, y):
        neighbors = []
        # Move right
        if self.is_valid(x, y + 1):
            neighbors.append((x, y + 1))
        # Move up
        if self.is_valid(x - 1, y):
            neighbors.append((x - 1, y))
        return neighbors

    def depth_first_search(self):
        stack = [(self.start, [self.start])]
        visited = set()
        while stack:
            (node, path) = stack.pop()
            if node == self.end:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor in self.get_neighbors(*node):
                    stack.append((neighbor, path + [neighbor]))
        return None

    def breadth_first_search(self):
        queue = deque([(self.start, [self.start])])
        visited = set()
        while queue:
            (node, path) = queue.popleft()
            if node == self.end:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor in self.get_neighbors(*node):
                    queue.append((neighbor, path + [neighbor]))
        return None

    def depth_limited_search(self, limit):
        stack = [(self.start, [self.start], 0)]
        visited = set()
        while stack:
            (node, path, depth) = stack.pop()
            if node == self.end:
                return path
            if depth < limit and node not in visited:
                visited.add(node)
                for neighbor in self.get_neighbors(*node):
                    stack.append((neighbor, path + [neighbor], depth + 1))
        return None

    def iterative_deepening_search(self):
        depth = 0
        while True:
            result = self.depth_limited_search(depth)
            if result is not None:
                return result
            depth += 1
            if depth > self.rows * self.cols:  # Prevent infinite loops in large grids
                return None

# Define the grid (predefined)
grid = [
    ['X', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', 'X']
]

# Take user input for start and end positions
start_position = tuple(map(int, input("Enter start position (row, col): ").split(',')))
end_position = tuple(map(int, input("Enter end position (row, col): ").split(',')))

# Create a Puzzle instance
puzzle = Puzzle(grid, start_position, end_position)

# Perform searches
print("Depth-First Search Path:", puzzle.depth_first_search())
print("Breadth-First Search Path:", puzzle.breadth_first_search())
print("Depth-Limited Search Path with limit 3:", puzzle.depth_limited_search(3))
print("Iterative Deepening Search Path:", puzzle.iterative_deepening_search())
