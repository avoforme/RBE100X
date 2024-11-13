from manhattan import Manhattan
from navigate import Navigate



navigate = Navigate((2, 2), 0, Manhattan())
for destination in [(3, 2), (3, 1), (5,1), (5,0)]:
    print('----------------')
    path = navigate.compute_path(destination)
    navigate.drive_path()
    print("Trip ended. Arrived at ", destination)
    print('----------------')

