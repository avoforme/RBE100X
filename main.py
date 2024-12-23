from manhattan import Manhattan
from navigate import Navigate
from dijkstra import Dijkstra
from grid import Grid

GRID_ROWS = 10
GRID_COLS = 5

# Create a grid
grid = Grid(GRID_ROWS, GRID_COLS)

# # Set some blocked nodes
# grid.set_blocked((2, 1))
# grid.set_blocked((0, 1))
# grid.set_blocked((1, 2))
# grid.set_blocked((3, 1))


# Connect neighbors in the grid
grid.connect_neighbors()

# Initialize Dijkstra algorithm
dijkstra = Dijkstra(grid)

current_location = (0, 0)
navigate = Navigate(current_location, 0, grid)

for destination in [(3,2), (2,1), (1,1)]:
    print('----------------')
    path = dijkstra.compute_path(current_location, destination)
    print(path) 
    
    while (path):
        finish_path = navigate.drive_path(path)
    
        if finish_path:
            print(f"Arrived at {destination}")
            break
        else:
            current_location = navigate.location
            path = dijkstra.compute_path(current_location, destination)
            print("Found intersection, new path: ", path)
            continue
    
                
    if not path:
        print(f"No path found to {destination}")
        continue
    
    if(len(path) > 0):
        current_location = navigate.location
    

    print('----------------')
