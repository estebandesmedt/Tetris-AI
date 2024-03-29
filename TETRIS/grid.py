import pygame
import random
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def __str__(self):
        grid_str = ""
        for row in self.grid:
            grid_str += " ".join(map(str, row)) + "\n"
        return grid_str


    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def get_rows(self):
        return len(self.grid) if self.grid else 0

    def clone(self):
        new_grid = Grid()
        new_grid.num_rows = self.num_rows
        new_grid.num_cols = self.num_cols
        new_grid.cell_size = self.cell_size
        new_grid.grid = [row[:] for row in self.grid]
        new_grid.colors = self.colors.copy()
        return new_grid

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def move_row_up(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row - num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def add_random_empty_row(self):
        new_row = [8] * self.num_cols

        empty_column = random.randint(0, self.num_cols - 1)
        new_row[empty_column] = 0  
        for row in range(self.num_rows - 1, 0, -1):
            self.grid[row] = self.grid[row - 1][:]
        self.grid[0] = new_row

    def move_up_and_add_row(self):
        self.move_row_up(0, 1)
        self.add_random_empty_row()
        self.grid[0] = [0] * self.num_cols

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows -1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
    
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0
    
    def draw(self, screen, x_offset=0, y_offset=0):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 11 + x_offset,
                                        row * self.cell_size + 11 + y_offset,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

