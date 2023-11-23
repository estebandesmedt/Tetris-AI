from colors import Colors
from position import Position
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, column):
        self.row_offset += rows
        self.column_offset += column

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    def clone(self):
        new_block = Block(self.id)
        new_block.cells = self.cells.copy()
        new_block.cell_size = self.cell_size
        new_block.row_offset = self.row_offset
        new_block.column_offset = self.column_offset
        new_block.rotation_state = self.rotation_state
        new_block.colors = self.colors.copy()
        return new_block
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) -1
            
    def draw(self, screen, offset_x, offset_y, custom_cell_size):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(
                offset_x + tile.column * custom_cell_size,
                offset_y + tile.row * custom_cell_size,
                custom_cell_size - 1,
                custom_cell_size - 1
            )
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
            