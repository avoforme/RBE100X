from dijkstra.grid import Grid
from dijkstra.dijkstra import Dijkstra


# Create a 5x5 grid
grid = Grid(5, 10)

# Set some blocked nodes
grid.set_blocked((1, 1))
grid.set_blocked((2, 2))
grid.set_blocked((3, 3))

# Connect neighbors in the grid
grid.connect_neighbors()

# Initialize Dijkstra algorithm
dijkstra = Dijkstra(grid)

# Compute and print the path from (0, 0) to (4, 4)
path = dijkstra.compute_path((0, 0), (4, 4))
