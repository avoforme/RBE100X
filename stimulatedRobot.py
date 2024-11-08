class StimulatedRobot:
    def __init__(self, location: tuple[int, int], heading: str, path) -> None:
        self.location = location
        self.heading = heading
        self.path = path
        
    # def drive_path(self, destination: tuple[int, int], heading: str):
    #     for 