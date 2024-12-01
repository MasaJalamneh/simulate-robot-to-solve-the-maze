from Algorithm import *
import API

# Depth First Search DFS algorithm for solving mazes, the maze is a set of paths that the robot can explore. 
# Start at the robot’s position, pick one direction and move as far along that path as possible.
# If a dead end or a visited place is reached, go back to the last place where other paths to try occur.
# Repeat this process until the goal is reached.
class DepthFirstSearch(Algorithm):

    def execute(self):

        API.log("DFS RUNNING...")

        # 0 > up, 1 > right, 2 > down, 3 > left
        orientation = 0
        current_position = [0, 0]  # start point

        stack = []  # Stack to keep track of the path
        visited = set()  # Set to keep track of visited nodes

        while MAZE_SETTINGS[current_position[0]][current_position[1]] != 0:

            self.update_maze_values()

            API.setColor(current_position[1], current_position[0], 'B')

            row, col = current_position
            front_wall = API.wallFront()
            right_wall = API.wallRight()
            left_wall = API.wallLeft()

            # Forward, Right, Left nodes
            neighbouring_nodes = [(), (), ()]
            neighbouring_values = [float("inf"), float("inf"), float("inf")]

            self.check_walls_around(front_wall, left_wall, right_wall, col, neighbouring_nodes, orientation, row, neighbouring_values)

            # If this node has already been visited, we skip it
            if (row, col) in visited:
                continue

            visited.add((row, col))  # mark this node as visited
            stack.append((row, col))  # add this node to the stack

            # If there's no way to move (dead-end), backtrack
            if front_wall and right_wall and left_wall:
                if stack:
                    prev_row, prev_col = stack.pop()  # backtrack to the previous node
                    current_position = [prev_row, prev_col]
                    continue

            # Explore the neighbors
            lowest_neighbor = min(neighbouring_values)
            orientation = self.choose_lowest_neighbour(col, current_position, lowest_neighbor, stack, orientation, row, neighbouring_values)

            cross_road = (not left_wall and not right_wall) or (not left_wall and not front_wall) or (not front_wall and not right_wall)

            if cross_road:
                # Mouse is making a new decision at a crossroad
                API.log(f"Crossroad at ({row}, {col})")

        API.log("FINISHED!!")

    def choose_lowest_neighbour(self, col, current_position, lowest_neighbor, stack, orientation, row, neighbouring_values):
        if lowest_neighbor == neighbouring_values[0]:  # Front
            API.moveForward()
            stack.append((row, col))  # Add current position to the stack

            if orientation == 0:
                current_position[0] += 1
            elif orientation == 1:
                current_position[1] += 1
            elif orientation == 2:
                current_position[0] -= 1
            elif orientation == 3:
                current_position[1] -= 1

        elif lowest_neighbor == neighbouring_values[1]:  # Right
            API.turnRight()
            API.moveForward()
            stack.append((row, col))  # Add current position to the stack

            if orientation == 0:
                current_position[1] += 1
                orientation = 1
            elif orientation == 1:
                current_position[0] -= 1
                orientation = 2
            elif orientation == 2:
                current_position[1] -= 1
                orientation = 3
            elif orientation == 3:
                current_position[0] += 1
                orientation = 0

        elif lowest_neighbor == neighbouring_values[2]:  # Left
            API.turnLeft()
            API.moveForward()
            stack.append((row, col))  # Add current position to the stack

            if orientation == 0:
                current_position[1] -= 1
                orientation = 3
            elif orientation == 1:
                current_position[0] += 1
                orientation = 0
            elif orientation == 2:
                current_position[1] += 1
                orientation = 1
            elif orientation == 3:
                current_position[0] -= 1
                orientation = 2

        return orientation

    def check_walls_around(self, front_wall, left_wall, right_wall, col, neighbouring_nodes, orientation, row, neighbouring_values):
        if not front_wall:
            if orientation == 0:
                front_val = MAZE_SETTINGS[row + 1][col]
                neighbouring_nodes[0] = (row + 1, col)
            elif orientation == 1:
                front_val = MAZE_SETTINGS[row][col + 1]
                neighbouring_nodes[0] = (row, col + 1)
            elif orientation == 2:
                front_val = MAZE_SETTINGS[row - 1][col]
                neighbouring_nodes[0] = (row - 1, col)
            elif orientation == 3:
                front_val = MAZE_SETTINGS[row][col - 1]
                neighbouring_nodes[0] = (row, col - 1)
            neighbouring_values[0] = front_val

        if not right_wall:
            if orientation == 0:
                right_val = MAZE_SETTINGS[row][col + 1]
                neighbouring_nodes[1] = (row, col + 1)
            elif orientation == 1:
                right_val = MAZE_SETTINGS[row - 1][col]
                neighbouring_nodes[1] = (row - 1, col)
            elif orientation == 2:
                right_val = MAZE_SETTINGS[row][col - 1]
                neighbouring_nodes[1] = (row, col - 1)
            elif orientation == 3:
                right_val = MAZE_SETTINGS[row + 1][col]
                neighbouring_nodes[1] = (row + 1, col)
            neighbouring_values[1] = right_val

        if not left_wall:
            if orientation == 0:
                left_val = MAZE_SETTINGS[row][col - 1]
                neighbouring_nodes[2] = (row, col - 1)
            elif orientation == 1:
                left_val = MAZE_SETTINGS[row + 1][col]
                neighbouring_nodes[2] = (row + 1, col)
            elif orientation == 2:
                left_val = MAZE_SETTINGS[row][col + 1]
                neighbouring_nodes[2] = (row, col + 1)
            elif orientation == 3:
                left_val = MAZE_SETTINGS[row - 1][col]
                neighbouring_nodes[2] = (row - 1, col)
            neighbouring_values[2] = left_val
