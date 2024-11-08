from stimulatedRobot import StimulatedRobot
class Navigate:
    def __init__(self, location: tuple[int, int], heading: str, algorithm) -> None:
        self.original_heading = heading
        self.heading = heading
        self.location = location
        self.algorithm = algorithm
        self.path = []

    def compute_path(self, destination: tuple[int, int]) -> list[tuple[int, int]]:
        self.path, self.heading = self.algorithm.compute_path(self.location, destination, self.heading)
        return self.path
    
    def print_path (self):
        print("Starting at ", self.location, " heading ", self.original_heading)
        print(self.path)
        print("Ending at ", self.path[-1], " heading ", self.heading)

   

