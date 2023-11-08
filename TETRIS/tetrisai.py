from game import Game

class TetrisAI:
    def __init__(self):
        # Define the parameters for the heuristic function
        self.a = -1 #height
        self.b = 10 #lines
        self.c = -100 #holes
        self.d = -1 #bumpiness

    def get_best_move(self, current_piece, grid, next_piece):
        best_move = None
        best_score = float('-inf')

        for rotation in range(4):
            for x in range(-5, 6):
                # print(rotation, x)
                temp_game = Game()
                temp_game.grid.grid = [row[:] for row in grid.grid]
                for _ in range(rotation):
                    temp_game.rotate()
                if x < 0:
                    for _ in range(abs(x)):
                        temp_game.move_left()
                elif x > 0:
                    for _ in range(x):
                        temp_game.move_right()

                score = self.calculate_score(temp_game.grid, current_piece, next_piece)
                if score > best_score:
                    best_score = score
                    best_move = (rotation, x)
        print(temp_game.grid)
        # print("Best Move:", best_move)
        return best_move

    def calculate_score(self, grid, current_piece, next_piece):
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
