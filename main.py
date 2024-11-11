import random

class Puzzle:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.position = start  # Current position of the robot
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0])

    def move(self, direction):
        current_x, current_y = self.position

        if direction == 0:  # Move right
            new_x, new_y = current_x, current_y + 1
        elif direction == 1:  # Move up
            new_x, new_y = current_x - 1, current_y
        else:
            return None  # Invalid direction

        # Check if the new position is within bounds and not blocked by an 'X'
        if 0 <= new_x < self.rows and 0 <= new_y < self.cols and self.grid[new_x][new_y] != 'X':
            self.position = (new_x, new_y)
            return self.position
        else:
            return None

    def is_solved(self):
        # Check if the current position matches the end position
        return self.position == self.end

    def play(self, k):
        for _ in range(k):
            if self.is_solved():
                print(f"Puzzle solved! Reached the end position at {self.position}")
                break
            possible_moves = [0, 1, 2, 3]  # 0 for Right, 1 for Up
            move = random.choice(possible_moves)
            result = self.move(move)
            if result is None:
                print(f"Move {move} failed. Current position: {self.position}")
            else:
                print(f"Move {move} successful. Current position: {self.position}")
        if not self.is_solved():
            print(f"Puzzle not solved. Current position: {self.position}")


grid = [
    
    ['X', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', 'X']

]

start_position = (2, 0)  # Start position
end_position = (0, 2)    # End position 

puzzle = Puzzle(grid, start_position, end_position)


puzzle.play(6)
