from dijkstra import Dijkstra
from grid import Grid

GRID_ROWS = 10
GRID_COLS = 5

# Create a grid
grid = Grid(GRID_ROWS, GRID_COLS)

# Set some blocked nodes
grid.set_blocked((1, 1))
grid.set_blocked((2, 2))
grid.set_blocked((3, 3))

# Connect neighbors in the grid
grid.connect_neighbors()

# Initialize Dijkstra algorithm
dijkstra = Dijkstra(grid)
print(dijkstra.compute_path((0,0), (4,4)))

