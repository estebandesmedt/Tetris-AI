from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        # pygame.mixer.music.load("Sounds/music.ogg")
        # pygame.mixer.music.play(-1)

    def apply_best_move(self, move):
        if move == "left" and not self.game_over:
            self.move_left()
        elif move == "right" and not self.game_over:
            self.move_right()
        elif move == "down" and not self.game_over:
            self.move_down()
        elif move == "rotate" and not self.game_over:
            self.rotate()
        elif move == "drop" and not self.game_over:
            self.drop_block()

    def apply_move(self, move):
        # Apply the specified move to the current block
        if move['rotation'] > 0:
            for _ in range(move['rotation']):
                self.rotate()

        if move['column'] < 0:
            for _ in range(abs(move['column'])):
                self.move_left()
        elif move['column'] > 0:
            for _ in range(move['column']):
                self.move_right()
        self.drop_block()

    def get_board(self):
        return self.grid.grid
    
    def update(self):
        if not self.game_over:
            self.move_down()

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500 
        self.score += move_down_points

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_to_left_side(self):
        while self.block_inside() and self.block_fits():
            self.current_block.move(0, -1)

        # If the block is now outside the grid or doesn't fit, move it back to the right
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, 1)

    def move_to_right_side(self):
        while self.block_inside() and self.block_fits():
            self.current_block.move(0, 1)

        # If the block is now outside the grid or doesn't fit, move it back to the right
        if not self.block_inside() or not self.block_fits():
            self.current_block.move(0, -1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def drop_block(self):
        while self.block_inside() and self.block_fits():
            self.current_block.move(1, 0)
        self.current_block.move(-1, 0)
        self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles: 
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def draw(self, screen, x_offset=0):
        self.grid.draw(screen, x_offset)
        self.current_block.draw(screen, 11 + x_offset, 11)
        
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255 + x_offset, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255 + x_offset, 280)
        else:
            self.next_block.draw(screen, 270 + x_offset, 270)
