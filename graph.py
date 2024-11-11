import networkx as nx
import matplotlib.pyplot as plt

# Define the grid and obstacles
grid = [
    ['X', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', 'X']
]

rows, cols = len(grid), len(grid[0])

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges based on the grid
for x in range(rows):
    for y in range(cols):
        if grid[x][y] != 'X':  # Only add nodes if not blocked
            G.add_node((x, y))
            # Add edge to the right
            if y + 1 < cols and grid[x][y + 1] != 'X':
                G.add_edge((x, y), (x, y + 1))
            # Add edge upwards
            if x - 1 >= 0 and grid[x - 1][y] != 'X':
                G.add_edge((x, y), (x - 1, y))

# Add the start and end nodes explicitly
G.add_node((2, 0))  # Start position
G.add_node((0, 2))  # End position

# Define positions for the nodes for better visualization
pos = {(x, y): (y, -x) for x in range(rows) for y in range(cols) if grid[x][y] != 'X'}
pos.update({(2, 0): (0, -2), (0, 2): (2, 0)})

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
plt.title("Problem Graph for Robot Movement")
plt.show()
