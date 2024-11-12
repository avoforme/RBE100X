from manhattan import Manhattan
from navigate import Navigate



navigate = Navigate((0, 0), 0, Manhattan())
for destination in [(4,3), (6,2), (0,1), (0,0)]:
    print('----------------')
    path = navigate.compute_path(destination)
    navigate.drive_path()
    print("Trip ended. Arrived at ", destination)
    print('----------------')

