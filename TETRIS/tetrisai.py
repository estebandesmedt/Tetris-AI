from game import Game
from blocks import *
import copy
import random

class TetrisAI:
    def __init__(self):
        # Define the parameters for the heuristic function
        self.a = -2 #height
        self.b = 1 #lines
        self.c = -1 #holes
        self.d = -1 #bumpiness

    def get_best_move(self, current_piece, grid):
        best_move = None
        best_score = float('-inf')

        for rotation in range(4):
            for x_col in range(-5, 6):
                temp_game = Game()
                temp_game.grid.grid = [row[:] for row in copy.deepcopy(grid.grid)]
                temp_game.current_block = copy.deepcopy(current_piece)  # Set the current block

                rotated_piece = copy.deepcopy(current_piece)
                for _ in range(rotation):
                    rotated_piece.rotate()

                rotated_piece.move(0, x_col)

                max_row_index = max(position.row for position in rotated_piece.get_cell_positions())
                row_offset = temp_game.grid.num_rows - max_row_index - 1

                for position in rotated_piece.get_cell_positions():
                    row_index = row_offset + position.row
                    col_index = position.column

                    if 0 <= row_index < temp_game.grid.num_rows and 0 <= col_index < temp_game.grid.num_cols:
                        temp_game.grid.grid[row_index][col_index] = rotated_piece.id


                print("\n" + "=" * 20 + "\n")
                print("Rotation:", rotation, "X:", x_col)
                print(temp_game.grid)
                print("\n" + "=" * 20 + "\n")

                # Calculate the score for the current placement
                score = self.calculate_score(temp_game.grid, rotated_piece)

                if score > best_score:
                    best_score = score
                    best_move = (rotation, x_col)

        print(temp_game.grid)
        print("Best Move:", best_move)
        # best_move = (random.randint(0,4), random.randint(-5,6))
        return best_move

    def calculate_score(self, grid, current_piece):
        aggregate_height = self.calculate_aggregate_height(grid)
        complete_lines = self.calculate_complete_lines(grid)
        holes = self.calculate_holes(grid)
        bumpiness = self.calculate_bumpiness(grid)

        score = (
            self.a * aggregate_height +
            self.b * complete_lines +
            self.c * holes +
            self.d * bumpiness
        )

        # print("Score:", score)
        return score

    def calculate_aggregate_height(self, grid):
        aggregate_height = 0
        heights = [0] * grid.num_cols

        for col in range(grid.num_cols):
            for row in range(grid.num_rows):
                if grid.grid[row][col] != 0:
                    heights[col] = grid.num_rows - row
                    break

        aggregate_height = sum(heights)
        # print(grid)
        # print("agg", aggregate_height)
        return aggregate_height

    def calculate_complete_lines(self, grid):
        completed_lines = 0
        for row in range(grid.num_rows):
            if all(cell != 0 for cell in grid.grid[row]):
                completed_lines += 1
        # print("lines", completed_lines)
        return completed_lines

    def calculate_holes(self, grid):
        height = grid.num_rows
        width = grid.num_cols
        holes = 0

        for col in range(width):
            hole_found = False
            for row in range(height):
                if grid.grid[row][col] == 0:
                    hole_found = True
                elif grid.grid[row][col] == 1 and hole_found:
                    holes += 1
        # print("holes", holes)
        return holes

    def calculate_bumpiness(self, grid):
        bumpiness = 0
        heights = [0] * grid.num_cols

        for col in range(grid.num_cols):
            for row in range(grid.num_rows):
                if grid.grid[row][col] != 0:
                    heights[col] = grid.num_rows - row
                    break

        for i in range(grid.num_cols - 1):
            bumpiness += abs(heights[i] - heights[i + 1])
        # print("bump", bumpiness)
        return bumpiness
    
    
