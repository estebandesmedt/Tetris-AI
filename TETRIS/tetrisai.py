import copy
import random

class TetrisAI:
    def __init__(self, tetris):
        self.tetris = tetris
        self.height_multiplier = 0.91
        self.holes_multiplier = 0.9
        self.lines_cleared_multiplier = 0.9
        self.bumpiness_multiplier = 0.9

    def reset(self):
        self.tetris.reset()

    def mutation(self):
            mutation_range = 0.1

            self.height_multiplier = max(0.5, min(2, round(self.height_multiplier + random.uniform(-mutation_range, mutation_range), 2)))
            self.lines_cleared_multiplier = max(0.5, min(2.5, round(self.lines_cleared_multiplier + random.uniform(-mutation_range, mutation_range), 2)))
            self.holes_multiplier = max(0.5, min(2, round(self.holes_multiplier + random.uniform(-mutation_range, mutation_range), 2)))
            self.bumpiness_multiplier = max(0.01, min(0.2, round(self.bumpiness_multiplier + random.uniform(-mutation_range, mutation_range), 2)))


    def evaluate_board(self, board):
        height_penalty = self.calculate_height_penalty(board)
        lines_cleared_bonus = self.calculate_lines_cleared_bonus(self.tetris)
        holes_penalty = self.calculate_holes_penalty(board)
        bumpiness_penalty = self.calculate_bumpiness_penalty(board)

        height_score = height_penalty * self.height_multiplier
        lines_score = lines_cleared_bonus * self.lines_cleared_multiplier
        holes_score = holes_penalty * self.holes_multiplier
        bumpiness_score = bumpiness_penalty * self.bumpiness_multiplier

        total_score = height_score + lines_score + holes_score + bumpiness_score

        return total_score
    
    def calculate_height_penalty(self, board):
        max_height = 0
        heights = [0] * len(board[0]) 
        for col in range(len(board[0])):
            for row in range(len(board)):
                if board[row][col] != 0:
                    heights[col] = len(board) - row
                    break
        max_height = max(heights)
        # print(max_height)
        return -max_height

    def calculate_lines_cleared_bonus(self, game_instance):
        cleared_lines = game_instance.clearedLines
        return cleared_lines
    
    def calculate_holes_penalty(self, board):
        holes = 0
        for col in zip(*board):
            hole_found = False
            for cell in col:
                if cell == 0 and hole_found:
                    holes += 1
                elif cell != 0:
                    hole_found = True
        # print(holes)
        return -holes

    def calculate_bumpiness_penalty(self, board):
        column_heights = [max(column) for column in zip(*board)]
        bumpiness = sum(abs(column_heights[i] - column_heights[i + 1]) for i in range(len(column_heights) - 1))
        # print(bumpiness)
        return -bumpiness

    def get_possible_moves(self):
        possible_moves = []

        for rotation in range(4):
            for column in range(-5, 6):
                move = {'rotation': rotation, 'column': column}
                possible_moves.append(move)

        return possible_moves

    def calculate_best_move(self):
        best_move = None
        best_score = float('-inf')

        for move in self.get_possible_moves():
            simulated_tetris = copy.deepcopy(self.tetris)

            simulated_tetris.apply_move(move)
            score = self.evaluate_board(simulated_tetris.get_board())
            if score > best_score:
                best_score = score
                best_move = move
        # print(best_move)
        return best_move
    
    def make_best_move(self):
        best_move = self.calculate_best_move()
        self.tetris.apply_move(best_move)

    #Genetic functions
    def apply_move(self, move):
        self.tetris.apply_move(move)

    def get_board(self):
        return self.tetris.get_board()
    
    def draw(self, screen, x_offset=0):
        self.tetris.draw(screen, x_offset)


#     def crossover(self, other_instance):
#         height_multiplier = self.crossoverHeight(other_instance.height_multiplier)
#         holes_multiplier = self.crossoverHoles(other_instance.holes_multiplier)
#         lines_cleared_multiplier = self.crossoverLines(other_instance.lines_cleared_multiplier)
#         bumpiness_multiplier = self.crossoverBumpiness(other_instance.bumpiness_multiplier)

#         # Create a new instance with the calculated multipliers
#         new_instance = TetrisAI(height_multiplier, holes_multiplier, lines_cleared_multiplier, bumpiness_multiplier)
        
#         return new_instance

#     def crossoverHeight(self, p2H):
#         p1H = self.height_multiplier
#         child_no_mutate = (p1H + p2H) / 2
#         child = child_no_mutate + random.uniform(-0.1, 0.1)
#         return child

#     def crossoverHoles(self, p2H):
#         p1H = self.holes_multiplier
#         child_no_mutate = (p1H + p2H) / 2
#         child = child_no_mutate + random.uniform(-0.1, 0.1)
#         return child

#     def crossoverLines(self, p2H):
#         p1H = self.lines_cleared_multiplier
#         child_no_mutate = (p1H + p2H) / 2
#         child = child_no_mutate + random.uniform(-0.1, 0.1)
#         return child

#     def crossoverBumpiness(self, p2H):
#         p1H = self.bumpiness_multiplier
#         child_no_mutate = (p1H + p2H) / 2
#         child = child_no_mutate + random.uniform(-0.1, 0.1)
#         return child

#     def __init__(self, height_multiplier, holes_multiplier, lines_cleared_multiplier, bumpiness_multiplier):
#         self.height_multiplier = height_multiplier
#         self.holes_multiplier = holes_multiplier
#         self.lines_cleared_multiplier = lines_cleared_multiplier
#         self.bumpiness_multiplier = bumpiness_multiplier

# # Example usage:
# # Assuming you have an instance called instance1
# instance1 = TetrisAI(1.0, 2.0, 3.0, 4.0)

# # Create another instance
# instance2 = TetrisAI(5.0, 6.0, 7.0, 8.0)

# # Call crossover method to create a new instance
# new_instance = instance1.crossover(instance2)
# print(new_instance.height_multiplier)



