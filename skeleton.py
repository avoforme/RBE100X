from XRPLib.defaults import drivetrain, reflectance

'''
Print reflectance values.
'''
def print_reflectance_values():
    left = reflectance.get_left()
    right = reflectance.get_right()
    
    print(f'Left: {left:.2f} | Right: {right:.2f} | Difference: {(left - right):.2f}')

'''
Drive forwards until hitting a line.
'''
def stop_at_line():
    pass

'''
Drive forwards until hitting a line, turn around, repeat.
'''
def stay_in_lines():
    pass

'''
Drive forwards, following the line.
'''
def follow_line():
    pass

'''
Drive forwards, following the line until hitting an intersection.
'''
def follow_line_until_intersection():
    pass


'''
Script here...
'''
while(True):
    print_reflectance_values()