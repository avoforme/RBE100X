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

for destination in [(3,2), (1,1)]:
    print('----------------')
    path = dijkstra.compute_path(current_location, destination)
    print(path) 
    
    while path:
        # Check if the next step in the path is blocked
        next_step = path[1] if len(path) > 1 else None
        
        # If the next step is blocked, remove it from the path
        if next_step and grid.get_node_at(next_step).blocked:
            print(f"Skipping blocked node {next_step}.")
            continue

        finish_path = navigate.drive_path(path)

        if finish_path:
            print(f"Arrived at {destination}")
            break
        else:
            # Update the current location
            current_location = navigate.location

            # Reinitialize Dijkstra to consider the updated blocked grid
            dijkstra = Dijkstra(grid)
            path = dijkstra.compute_path(current_location, destination)

            print("Found obstacle, recalculated path: ", path)
            continue

    
                
    if not path:
        print(f"No path found to {destination}")
        continue
    
    if(len(path) > 0):
        current_location = navigate.location
    

    print('----------------')
