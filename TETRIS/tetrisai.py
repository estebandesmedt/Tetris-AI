import copy

class TetrisAI:
    def __init__(self, tetris):
        self.tetris = tetris  
        self.height_multiplier = 0.1
        self.lines_cleared_multiplier = 1
        self.holes_multiplier = 0.1
        self.bumpiness_multiplier = 0.1

    def evaluate_board(self, board):
        height_penalty = self.calculate_height_penalty(board)
        lines_cleared_bonus = self.calculate_lines_cleared_bonus(board)
        holes_penalty = self.calculate_holes_penalty(board)
        bumpiness_penalty = self.calculate_bumpiness_penalty(board)

        # Apply multipliers to each component
        height_score = height_penalty * self.height_multiplier
        lines_score = lines_cleared_bonus * self.lines_cleared_multiplier
        holes_score = holes_penalty * self.holes_multiplier
        bumpiness_score = bumpiness_penalty * self.bumpiness_multiplier

        # Combine the four components into an overall score
        total_score = height_score + lines_score + holes_score + bumpiness_score

        return total_score
    
    def calculate_height_penalty(self, board):
        # Penalize higher columns to encourage a lower stack
        max_height = max([max(column) for column in zip(*board)])
        print(max_height)
        return -max_height

    def calculate_lines_cleared_bonus(self, board):
        # Provide a bonus for cleared lines to encourage clearing lines
        lines_cleared = sum([1 for row in board if all(cell != 0 for cell in row)])
        return lines_cleared
    
    def calculate_holes_penalty(self, board):
        # Penalize the number of holes in the stack
        holes = 0
        for col in zip(*board):
            hole_found = False
            for cell in col:
                if cell == 0 and hole_found:
                    holes += 1
                elif cell != 0:
                    hole_found = True
        print(holes)
        return -holes

    def calculate_bumpiness_penalty(self, board):
        # Penalize the difference in height between adjacent columns to reduce bumpiness
        column_heights = [max(column) for column in zip(*board)]
        bumpiness = sum(abs(column_heights[i] - column_heights[i + 1]) for i in range(len(column_heights) - 1))
        return -bumpiness

    def get_possible_moves(self):
        # Generate all possible moves (rotations and translations) for the current piece
        possible_moves = []

        for rotation in range(4):
            for column in range(-5, 6):
                move = {'rotation': rotation, 'column': column}
                possible_moves.append(move)

        return possible_moves

    def calculate_best_move(self):
        best_move = None
        best_score = float('-inf')

        # Iterate through all possible moves
        for move in self.get_possible_moves():
            # Create a deep copy of the current game state to simulate the move
            simulated_tetris = copy.deepcopy(self.tetris)

            # Apply the move to the simulated game state
            simulated_tetris.apply_move(move)

            # Evaluate the new game state
            score = self.evaluate_board(simulated_tetris.get_board())

            # Update the best move if the new score is better
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def make_best_move(self):
        # Get the best move and apply it to the actual game state
        best_move = self.calculate_best_move()
        self.tetris.apply_move(best_move)
