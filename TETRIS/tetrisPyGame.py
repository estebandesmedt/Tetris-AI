import pygame, sys
import time
from game import Game
from colors import Colors
from tetrisai import TetrisAI

pygame.init()
start_time = time.time()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
paused_surface = title_font.render("PAUSED", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()
tetris_ai = TetrisAI(game)

GAME_UPDATE = pygame.USEREVENT
GAME_SPEED = 200
pygame.time.set_timer(GAME_UPDATE, GAME_SPEED)

paused = False

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
            if event.key == pygame.K_SPACE and not game.game_over:
                game.drop_block()
            if event.key == pygame.K_p:
                paused = not paused  # Toggle pause state
        if event.type == GAME_UPDATE and not game.game_over and not paused:
            game.move_down()
        if not game.game_over and not paused:
            tetris_ai.make_best_move()
            game.update()

    # Continue with game logic
    current_piece = game.current_block
    next_piece = game.next_block
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))
    elif paused:
        screen.blit(paused_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface,
                score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
