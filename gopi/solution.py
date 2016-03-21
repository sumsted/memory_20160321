import robot
'''
We import robot. This lets us call all of the functions in robot.py.

We set robot_debug to True to test our code without sending it to the robot.
Set robot_debug to False when you are ready to run your code on the robot.
'''
robot.robot_debug = False

robot.robot_speed = 150

robot.forward(1.0)
robot.forward(1.0)
robot.left(1.0)
robot.right(1.0)
robot.blink(10)
robot.forward(1.0)

#
# robot.robot_speed = 125
# robot.forward(3)
# robot.right_rot(.7)
# robot.forward(2.5)
# robot.left_rot(.7)
# robot.forward(5)
# robot.forward(4)
# robot.left_rot(.7)
# robot.forward(3)
#
# robot.forward(3)
# robot.right_rot(.7)
# robot.forward(3)
# robot.stop()

'''

These are all the functions you can call in robot.

robot.backward(1.0)
robot.forward(1.0)
robot.left(1.0)
robot.right(1.0)
robot.left_rot(1.0)
robot.right_rot(1.0)
robot.stop(1.0)
robot.blink()
d = robot.distance()
v = robot.volt()

'''

'''
Navigate the course. All of the direction functions may take seconds as a parameter, 0.2 to 5.0.
'''


'''
The servo may be moved from 0 to 180 degrees.
How might you use a loop to print the range from 0 to 180 degrees in 10 degree increments?
'''

'''
Can you write a function to make the perform a certain task, then call this function from a loop?
'''
