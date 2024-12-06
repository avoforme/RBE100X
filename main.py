from manhattan import Manhattan
from navigate import Navigate


manhattan = Manhattan()
navigate = Navigate((2, 2), 0)
for destination in [(4,3), (6,2), (1,1)]:
    print('----------------')
    path = manhattan.compute_path(navigate.location, destination)
    print(path)
    navigate.drive_path(path)
    print("Trip ended. Arrived at ", destination)
    print('----------------')


