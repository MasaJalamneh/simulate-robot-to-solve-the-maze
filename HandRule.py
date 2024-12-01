from Algorithm import *
import API

# Left Hand rule, the priority is for going left if we can, 
# if there is a wall on the left then go strait, if there is a wall then go right, 
# if there is a wall then rotate 180 degrees and go backward
class LeftHandRule(Algorithm):

    def execute(self):
        API.log("LEFT HAND RULE RUNNING...")

        current_position = [0, 0]
        orientation = 0

        while True:
            # Check if the goal is reached
            if check_end_point(current_position):
                break

            # Check if the left path is open
            if not API.wallLeft():
                API.turnLeft()
                orientation = (orientation - 1) % 4

            # Check if the forward path is open
            while API.wallFront():
                API.turnRight()
                orientation = (orientation + 1) % 4

            # If the left path is closed by wall, move forward 
            API.moveForward()

            if orientation == 0:
                current_position[1] += 1
            elif orientation == 1:
                current_position[0] += 1
            elif orientation == 2:
                current_position[1] -= 1
            elif orientation == 3:
                current_position[0] -= 1

            # Set the colour of the path that the mouse move in to green
            API.setColor(current_position[0], current_position[1], 'G')
            

# Right Hand rule, the priority is for going right if we can, 
# if there is a wall on the right then go strait, if there is a wall then go left, 
# if there is a wall then rotate 180 degrees and go backward
class RightHandRule(Algorithm):

    def execute(self):
        API.log("RIGHT HAND RULE RUNNING...")

        current_position = [0, 0]
        orientation = 0

        while True:
            # Check if the goal is reached
            if check_end_point(current_position):
                break

            # Check if the right path is open
            if not API.wallRight():
                API.turnRight()
                orientation = (orientation + 1) % 4

            # Check if the Forward path is open
            while API.wallFront():
                API.turnLeft()
                orientation = (orientation - 1) % 4

            # If the right path is closed by wall, move forward
            API.moveForward()

            if orientation == 0:
                current_position[1] += 1
            elif orientation == 1:
                current_position[0] += 1
            elif orientation == 2:
                current_position[1] -= 1
            elif orientation == 3:
                current_position[0] -= 1

            # Set the colour of the path that the mouse move in to green
            API.setColor(current_position[0], current_position[1], 'G')