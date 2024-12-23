from dijkstra import Dijkstra
from grid import Grid
from navigate import Navigate

GRID_ROWS = 10
GRID_COLS = 5

# Create a grid
grid = Grid(GRID_ROWS, GRID_COLS)

# Set some blocked nodes
grid.set_blocked((1, 1))
grid.set_blocked((2, 2))

# Connect neighbors in the grid
grid.connect_neighbors()

# Initialize Dijkstra algorithm
dijkstra = Dijkstra(grid)
path = dijkstra.compute_path((0,0), (3,3))
print(path)

navigate = Navigate((0, 0), 0, grid)
navigate.drive_path(path)  # Drive the computed path
