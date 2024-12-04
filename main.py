from navigate import Navigate
from dijkstra.dijkstra import Dijkstra
from manhattan import Manhattan

# Initialize Navigate with starting location, initial heading, and the Dijkstra algorithm
GRID_ROWS = 10
GRID_COLS = 5
# dijkstra_algorithm = Dijkstra(GRID_ROWS, GRID_COLS)
# navigate = Navigate((2, 2), 0, dijkstra_algorithm) 
navigate = Navigate((0, 0), 0, Manhattan())

# Define destinations and navigate to each
for destination in [(4, 3), (6, 2), (1, 1)]:
    print('----------------')
    print(f"Computing path to destination: ", destination)
    path = navigate.compute_path(destination)  # Compute path to the destination
    print(f"Path: ", path)
    # navigate.drive_path()  # Drive the computed path
    print(f"Trip ended. Arrived at ", destination)
    print('----------------')
