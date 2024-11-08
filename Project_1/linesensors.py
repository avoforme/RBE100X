from XRPLib.reflectance import Reflectance

# about 0.90 black
# about 0.50 white

class LineSensors:
    '''
    This class is encapsulates the functionality required from the reflectance
    sensors for navigating around the grid. It would allow one to change to a
    different line sensor, and by changing these methods, the rest of the program
    would keep working.
    '''
    def __init__(self) -> None:
        '''
        Instantiate a default reflectance sensor object
        '''
        self.reflectance = Reflectance.get_default_reflectance()

    def get_error(self) -> float:
        '''
        Return the error value that can be used for proportional control
        driving for line following
        '''
        return self.reflectance.get_left() - self.reflectance.get_right()

    def at_cross(self) -> bool:
        '''
        Return true if the line tracking sensors are above an intersecton (cross)
        This is true if both sensors are seeingn a black level
        '''
        return self.reflectance.get_left() >= 0.9 and self.reflectance.get_right() >= 0.9
    
    # def either_on_line(self) -> bool:
    #     '''
    #     Return true if either of the sensors is on a taped line
    #     This is useful for making turns back to the line when turning around
    #     or looking for an intersection while the robot is turning.
    #     '''
    #     pass
            

    def report_values(self) -> None:
        '''
        Print the left and right values from the line tracking sensor for debugging
        '''
        left = self.reflectance.get_left()
        right = self.reflectance.get_right()
        print(f'Left: {left:.2f} | Right: {right:.2f} | Difference: {(left - right):.2f}')

 