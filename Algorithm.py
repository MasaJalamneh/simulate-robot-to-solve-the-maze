from abc import ABC, abstractmethod
import API

# Define the maze settings, so that the goal is the four locations in the center and has 0 values
MAZE_SETTINGS = [
    [14, 13, 12, 11, 10, 9, 8, 7, 7, 8, 9, 10, 11, 12, 13, 14],
    [13, 12, 11, 10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 11, 12, 13],
    [12, 11, 10, 9, 8, 7, 6, 5, 5, 6, 7, 8, 9, 10, 11, 12],
    [11, 10, 9, 8, 7, 6, 5, 4, 4, 5, 6, 7, 8, 9, 10, 11],
    [10, 9, 8, 7, 6, 5, 4, 3, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 8, 7, 6, 5, 4, 3, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8],
    [7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7],
    [7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6, 7],
    [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8],
    [9, 8, 7, 6, 5, 4, 3, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    [10, 9, 8, 7, 6, 5, 4, 3, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 10, 9, 8, 7, 6, 5, 4, 4, 5, 6, 7, 8, 9, 10, 11],
    [12, 11, 10, 9, 8, 7, 6, 5, 5, 6, 7, 8, 9, 10, 11, 12],
    [13, 12, 11, 10, 9, 8, 7, 6, 6, 7, 8, 9, 10, 11, 12, 13],
    [14, 13, 12, 11, 10, 9, 8, 7, 7, 8, 9, 10, 11, 12, 13, 14]
]
# Define location of the center of the maze
CENTER = len(MAZE_SETTINGS) // 2

# Function used to check if the object is in the goal, used in Hand rule algorithm
def check_end_point(current_position):
        if (current_position[0] == CENTER and current_position[1] == CENTER) or (
                current_position[0] == CENTER - 1 and current_position[1] == CENTER - 1) or (
                current_position[0] == CENTER - 1 and current_position[1] == CENTER) or (
                current_position[0] == CENTER and current_position[1] == CENTER - 1):
            return True

# Define Algorithm class, contains common functions to be shared between all the algorithms
class Algorithm(ABC):
    def update_maze_values(self):
        for i in range(16):
            for j in range(16):
                API.setText(i, j, str(MAZE_SETTINGS[i][j]))

    @abstractmethod
    def execute(self):
        pass
