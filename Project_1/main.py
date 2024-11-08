# this program uses the LineTrack and LineSensors classes to track around the circle,
# and turn around at the cross.
# Students would just be writing the line following code as a set of functions to do
# the various operations at this point (Project 1). For Project 2, they would
# refactor this code into classes, then go on to doing grid navigation with it

from Project_1.linetrack import LineTrack

print("Starting")
lt = LineTrack()

# track around the circle 4 times
for times in range(4):
    
    print(f'This is the: {times + 1} time')
    
    # track the circle
    lt.track_to_intersection()

    # the first time running, the robot should turn right to the center of the circle. set the robot correctly when testing

    # the first and third time, the robot should turn right
    if times%2 == 0:
        lt.turn_clockwise()
    # the second and fourth time, the robot should turn left
    else:
        lt.turn_counterclockwise()

print("finished")