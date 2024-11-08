from manhattan import Manhattan
from navigate import Navigate


# path = Manhattan.compute_path((4, 4), (3, 3))
# print(path)

navigate = Navigate((0, 0), "N", Manhattan())
navigate.compute_path((2, 2))
navigate.print_path()