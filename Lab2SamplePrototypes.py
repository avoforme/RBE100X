# working code

# Lab 2 sample function prototypes. You should get each of these functions working

# imports that might be useful to implement the functions that are defined
# throughought this file.
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.rangefinder import Rangefinder
from XRPLib.reflectance import Reflectance
from XRPLib.timeout import time
from XRPLib.board import Board

# instances of classes that are likely useful to implement the functions in this file
drive = DifferentialDrive.get_default_differential_drive()
line = Reflectance.get_default_reflectance()
dist = Rangefinder.get_default_rangefinder()
board = Board.get_default_board()

# values for my light sensors that indicate approximate whiteboard and tape values
# 0.9 is on the line
# 0.5 is off the line

# a good value to differentiate between light and dark
THRESHOLD = 0.65
BLACK = 0.9
WHITE = 0.5

# you should replace the "raise NotImplementedError" exception with the correct code
# for each of these functions. The get progressively more complex, so I suggest that
# you start at the first one and make them work one at a time.
# When you are ready to test one of the functions, uncomment the corresponding like
# of code at the bottom of the file and the function will run.
# Hint: the last function can probably make use of some of the others to implememt it

'''
Print reflectance values.
'''
def print_reflectance_values():
    left = line.get_left()
    right = line.get_right()
    
    print(f'Left: {left:.2f} | Right: {right:.2f} | Difference: {(left - right):.2f}')
    
def stop_at_line():
    '''
    This drives the robot forward until it hits a line, then stops
    '''
    while True:
        print_reflectance_values()
        drive.set_speed(20, 20)

        if line.get_left() >= 0.9 and line.get_right() >= 0.9:
            print("Line detected, stopping")
            drive.stop()
            break
    raise NotImplementedError()

def stay_in_circle():

    '''
    Keep the robot within a circle by
    turning around whenever the line sensors see a line
    '''

        

    raise NotImplementedError()


def follow_line():
    '''
    Follow a line forever
    '''
    original_effort = 25
    left_effort = original_effort
    right_effort = original_effort
    drive.set_speed(left_effort, right_effort)
    
    while True:
        left = line.get_left()
        right = line.get_right()
        propto_effort = (left - right) * 25
        print('____')
        print(f'Left: {left:.2f} | Right: {right:.2f} | Difference: {(left - right):.2f}')
        print(f'Left effort: {left_effort:.2f} | Right effort: {right_effort:.2f} | Prototo effort:  {propto_effort:.2f}')
        
        if line.get_left() >= 0.9 and line.get_right() >= 0.9:
            print("Line detected, turning")
            drive.turn(-180)

        if abs(left - right) > 0.1:
            left_effort = original_effort - propto_effort
            right_effort = original_effort + propto_effort
            drive.set_speed(left_effort, right_effort)
        else:
            left_effort = original_effort
            right_effort = original_effort
            drive.set_speed(left_effort, right_effort)
    raise NotImplementedError()

follow_line()

def follow_line_until_cross():
    '''
    Follow a line until we hit a cross, then stop
    '''
    raise NotImplementedError()


def turn_around():
    '''
    Turn around to pick up the line going the other way
    Turn 60 degrees to get off the line, then keep turning until
    the robot picks up the line again
    '''
    while True:
        drive.set_speed(20, 20)
        if line.get_left() >= 0.9 and line.get_right() >= 0.9:
            print("Line detected, turning")
            drive.turn(180)
    raise NotImplementedError()

def follow_and_turn_around():
    '''
    Follow the line until hitting the cross, then turn around and
    track until hitting it again. Repeat this twice to be sure.
    '''
    raise NotImplementedError()

# you can test each of the above functions by uncommenting one of the lines below
# and trying it. Then once it is working, comment it again, and uncomment the next one
# and keep going until you have gotten them all to work.
    
# stop_at_line()
# while(True):
# print_reflectance_values()
# stay_in_circle()
# follow_line_until_cross()
# turn_around()
# follow_and_turn_around()

