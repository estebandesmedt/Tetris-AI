class TetrisAI:
    def __init__(self):
        # Define the parameters for the heuristic function
        self.a = -0.510066
        self.b = 0.760666
        self.c = -0.35663
        self.d = -0.184483

    def get_best_move(self, current_piece, grid, next_piece):
        best_move = None
        best_score = float('-inf')

        for rotation in range(4):
            for x in range(-5, 6):
                temp_game = TetrisGame(grid.copy())
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

        return best_move

    def calculate_score(self, grid, current_piece, next_piece):
        # Calculate the heuristics
        aggregate_height = self.calculate_aggregate_height(grid)
        complete_lines = self.calculate_complete_lines(grid)
        holes = self.calculate_holes(grid)
        bumpiness = self.calculate_bumpiness(grid)

        # Calculate the score using the linear combination of heuristics
        score = (
            self.a * aggregate_height +
            self.b * complete_lines +
            self.c * holes +
            self.d * bumpiness
        )

        return score

    def calculate_aggregate_height(self, grid):
        heights = [0] * 10
        for row in range(20):
            for col in range(10):
                if grid[row][col] != 0:
                    heights[col] = 20 - row
        aggregate_height = sum(heights)
        return aggregate_height

    def calculate_complete_lines(self, grid):
        complete_lines = 0
        for row in range(20):
            if all(grid[row]):
                complete_lines += 1
        return complete_lines

    def calculate_holes(self, grid):
        holes = 0
        for col in range(10):
            for row in range(19, 0, -1):
                if grid[row][col] == 0 and any(grid[i][col] != 0 for i in range(row)):
                    holes += 1
        return holes

    def calculate_bumpiness(self, grid):
        bumpiness = 0
        for col in range(9):
            bumpiness += abs(sum(grid[row][col] for row in range(20)) - sum(grid[row][col + 1] for row in range(20)))
        return bumpiness

class TetrisGame:
    def __init__(self, grid):
        self.grid = [list(row) for row in grid]

    def rotate(self):
        self.grid = list(zip(*self.grid[::-1]))

    def move_left(self):
        self.grid = [row[1:] + [0] for row in self.grid]

    def move_right(self):
        self.grid = [row[:-1] + [0] for row in self.grid]


