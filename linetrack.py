from XRPLib.differential_drive import DifferentialDrive
from linesensors import LineSensors

class LineTrack:
    '''
    Line_Track class deals with driving the robot on a board with a taped line
    this class includes code for calibrating the line sensors and finding a
    threshold value for knowing if the robot is on or off the line.
    '''
    # TURN_SPEED: float = 0.40
    DRIVE_SPEED: float = 20
    Kp: float = 25
    # DIST_TO_CENTER: float = 8.75

    def __init__(self) -> None:
        '''
        Create a line tracking sensor
        '''
        self.drivetrain = DifferentialDrive.get_default_differential_drive()
        self.line_sense = LineSensors()
        

    def track_to_intersection(self) -> None:
        '''
        Track the line using proportional control.
        The difference between line tracking sensors is used to generate an error value
        that is used to proportionally drive the robot with the arcade method
        '''
        original_effort = self.DRIVE_SPEED
        left_effort = original_effort
        right_effort = original_effort
        self.drivetrain.set_speed(left_effort, right_effort)
        
        while True:
            # proportional correction effort
            propto_effort = self.line_sense.get_error() * self.Kp

            # if the robot is at an intersection, stop
            if self.line_sense.at_cross():
                self.drivetrain.stop()
                break
            
            # if the robot is off the line, correct it
            if abs(self.line_sense.get_error()) > 0.1:
                left_effort = original_effort - propto_effort
                right_effort = original_effort + propto_effort
                self.drivetrain.set_speed(left_effort, right_effort)
            else:
                left_effort = original_effort
                right_effort = original_effort
                self.drivetrain.set_speed(left_effort, right_effort)


    def turn_clockwise(self) -> None:
        '''
        Make a turn in the clockwise direction to the intersection line
        This could either be towards a perpendicular line in the grid or it could 
        be for a 180 turn on a circle, the turning until reintercepting the line.
        '''
        print("Line detected, turning")
        self.drivetrain.turn(-180)


    def turn_counterclockwise(self) -> None:
        '''
        Make a turn in the counterclockwise direction to the intersection line
        This could either be towards a perpendicular line in the grid or it could 
        be for a 180 turn on a circle, the turning until reintercepting the line.
        '''
        self.drivetrain.turn(180)


    # def drive_past_intersection(self) -> None:
    #     '''
    #     Drive the robot past the interection that it just stopped at so that the
    #     same intersection won't be immediatly detected again as another intersection.
    #     '''
    #     pass



