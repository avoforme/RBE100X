from manhattan import Manhattan
from navigate import Navigate
from dijkstra import Dijkstra
from grid import Grid

GRID_ROWS = 10
GRID_COLS = 5

# Create a grid
grid = Grid(GRID_ROWS, GRID_COLS)

# Set some blocked nodes
grid.set_blocked((2, 1))
grid.set_blocked((0, 1))
grid.set_blocked((1, 2))
grid.set_blocked((3, 1))


# Connect neighbors in the grid
grid.connect_neighbors()

# Initialize Dijkstra algorithm
dijkstra = Dijkstra(grid)

current_location = (0, 0)
navigate = Navigate(current_location, 0)

for destination in [(3,2), (2,1), (1,1)]:
    print('----------------')
    path = dijkstra.compute_path(current_location, destination)
    print(path)
    navigate.drive_path(path)
    print("Trip ended. Arrived at ", destination)
    if(len(path) > 0):
        current_location = destination

    print('----------------')
