import pygame, sys
import time
from game import Game
from colors import Colors
from grid import Grid
from tetrisai import TetrisAI

pygame.init()
start_time = time.time()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()
tetris_ai =  TetrisAI()

GAME_UPDATE = pygame.USEREVENT
GAME_SPEED = 200
pygame.time.set_timer(GAME_UPDATE, GAME_SPEED)

while True:
    elapsed_time = time.time() - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    # Calculate AI's move
    best_move = tetris_ai.get_best_move(game.current_block, game.grid, game.next_block)
    if best_move is not None:
        rotation, x = best_move
        for _ in range(rotation):
            game.rotate()
        if x < 0:
            for _ in range(abs(x)):
                game.move_left()
        elif x > 0:
            for _ in range(x):
                game.move_right()

    # Continue with game logic
    current_piece = game.current_block
    next_piece = game.next_block

    best_move = tetris_ai.get_best_move(current_piece, game.grid, next_piece)
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)