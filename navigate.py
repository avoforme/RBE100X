from linesensors import LineSensors
from linetrack import LineTrack
class Navigate:
    DIRECTION = ["N", "E", "S", "W"]
    '''
    Navigate is a class designed to manage movement from one location to another on a grid. 
    It calculates and drives the shortest path between points by determining necessary heading 
    adjustments to achieve correct alignment and positioning.
    
    '''
    def __init__(self, location: tuple[int, int], heading: int, algorithm) -> None:
        '''
        Initializes the Navigate object with a starting location, heading, and pathfinding algorithm.
        '''
        self.linetrack = LineTrack()
        self.heading = heading
        self.location = location
        self.algorithm = algorithm
        self.path = []

    def compute_path(self, destination: tuple[int, int]) -> list[tuple[int, int]]:       
        '''
        Computes the shortest path from the current location to the destination using the specified algorithm.
        ''' 

        print("Starting at ", self.location)
        self.path = self.algorithm.compute_path(self.location, destination)
        print(self.path)
        print("Ending at ", self.path[-1])
        return self.path

    
    def drive_to(self, location: tuple[int, int]) -> None:
        '''
        Moves from the current location to a specified adjacent location, adjusts the
        heading and then updates the position.

        '''
        current_heading = self.heading
        current_row, current_col = self.location
        end_row, end_col = location

        # move one row up
        if current_row + 1 == end_row:
            print("Moving up from ", self.location, " to ", location)
            print("Current heading is ", current_heading)
            self.heading = self.linetrack.turn_then_track(current_heading, 0)
            print("New heading is ", self.heading)
            current_row += 1
            # if current_heading != "N":  
            #     current_heading = "N"
                
                
        # move one row down
        elif current_row -1 == end_row:
            print("Moving down from ", self.location, " to ", location)
            print("Current heading is ", current_heading)
            self.heading = self.linetrack.turn_then_track(current_heading, 2)
            print("New heading is ", self.heading)

            current_row -= 1
                # if current_heading != "S": 
                #     current_heading = "S"

        # move one column right
        elif current_col +1 == end_col:
            print("Moving right from ", self.location, " to ", location)
            print("Current heading is ", current_heading)
            self.heading = self.linetrack.turn_then_track(current_heading, 1)
            print("New heading is ", self.heading)

            current_col += 1
                # if current_heading != "E": 
                #     current_heading = "E"

        # move one column left
        elif current_col -1 == end_col:
            print("Moving left from ", self.location, " to ", location)

            print("Current heading is ", current_heading)
            self.heading = self.linetrack.turn_then_track(current_heading, 3)
            print("New heading is ", self.heading)

            current_col -= 1
                # if current_heading != "W":  
                #     current_heading = "W"

        self.location = (current_row, current_col)
        
    def drive_path(self) -> None:
        '''
        Drives along the precomputed path by calling drive_to() for each location in the path.
        '''
        for location in self.path:
            self.drive_to(location)
   

