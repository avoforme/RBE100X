from linesensors import LineSensors
from linetrack import LineTrack
from XRPLib.rangefinder import Rangefinder

class Navigate:
    DIRECTION = ["N", "E", "S", "W"]
    '''
    Navigate is a class designed to manage movement from one location to another on a grid. 
    It calculates and drives the shortest path between points by determining necessary heading 
    adjustments to achieve correct alignment and positioning.
    
    '''
    def __init__(self, location: tuple[int, int], heading: int, grid) -> None:
        '''
        Initializes the Navigate object with a starting location, heading, and pathfinding algorithm.
        '''
        self.my_grid = grid
        self.linetrack = LineTrack()
        self.heading = heading
        self.location = location
        self.rangefinder = Rangefinder.get_default_rangefinder()


    def drive_to(self, location: tuple[int, int]) -> bool:
        '''
        Moves from the current location to a specified adjacent location, adjusts the
        heading and then updates the position.
        
        Returns True if an obstacle is detected, False otherwise.
        '''
        
        current_heading = self.heading
        current_row, current_col = self.location
        end_row, end_col = location

        # move one row up
        if current_row + 1 == end_row:
            self.heading = self.linetrack.turn_then_no_track(current_heading, 0)
            if self.detect_obstacle():
                self.my_grid.set_blocked(location)
                return True
            self.linetrack.after_turn()
            current_row += 1
                
        # move one row down
        elif current_row -1 == end_row:
            self.heading = self.linetrack.turn_then_no_track(current_heading, 2)
            if self.detect_obstacle():
                self.my_grid.set_blocked(location)
                return True
            self.linetrack.after_turn() 
            current_row -= 1
        
        # move one column right
        elif current_col +1 == end_col:
            self.heading = self.linetrack.turn_then_no_track(current_heading, 1)
            if self.detect_obstacle():
                self.my_grid.set_blocked(location)
                return True
            self.linetrack.after_turn()
            current_col += 1   

        # move one column left
        elif current_col -1 == end_col:
            self.heading = self.linetrack.turn_then_no_track(current_heading, 3)
            if self.detect_obstacle():
                self.my_grid.set_blocked(location)
                return True
            self.linetrack.after_turn()
            current_col -= 1

        self.location = (current_row, current_col)
        return False
        
    def drive_path(self, path) -> bool:
        '''
        Drives along the precomputed path by calling drive_to() for each location in the path.
        
        Returns True if the path is completed, False if an obstacle is detected.
        '''
        for location in path:
            is_blocked = self.drive_to(location)
            if is_blocked:
                return False
        return True
   
    def detect_obstacle(self) -> bool:
        '''
        Use the rangefinder to check if there is an obstacle within 10 cm.
        '''
        distance = self.rangefinder.distance()
        print(f"Rangefinder distance: {distance} cm")
        return distance < 10
