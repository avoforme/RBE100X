from linesensors import LineSensors
from linetrack import LineTrack
class Navigate:
    DIRECTION = ["N", "E", "S", "W"]
    '''
    Navigate is a class designed to manage movement from one location to another on a grid. 
    It calculates and drives the shortest path between points by determining necessary heading 
    adjustments to achieve correct alignment and positioning.
    
    '''
    def __init__(self, location: tuple[int, int], heading: int) -> None:
        '''
        Initializes the Navigate object with a starting location, heading, and pathfinding algorithm.
        '''
        self.linetrack = LineTrack()
        self.heading = heading
        self.location = location

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
            self.heading = self.linetrack.turn_then_track(current_heading, 0)
            current_row += 1
                
        # move one row down
        elif current_row -1 == end_row:
            self.heading = self.linetrack.turn_then_track(current_heading, 2)
            current_row -= 1
            
        # move one column right
        elif current_col +1 == end_col:
            self.heading = self.linetrack.turn_then_track(current_heading, 1)
            current_col += 1                

        # move one column left
        elif current_col -1 == end_col:
            self.heading = self.linetrack.turn_then_track(current_heading, 3)
            current_col -= 1

        self.location = (current_row, current_col)
        
    def drive_path(self, path) -> None:
        '''
        Drives along the precomputed path by calling drive_to() for each location in the path.
        '''
        for location in path:
            self.drive_to(location)
   

