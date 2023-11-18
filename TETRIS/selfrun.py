import pygame, sys
import os
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

# player1
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
# player2
score_rect2 = pygame.Rect(820, 55, 170, 60)
next_rect2 = pygame.Rect(820, 215, 170, 180)

screen = pygame.display.set_mode((1000, 620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

gamePlayer = Game()
gameAI = Game()
tetris_ai = TetrisAI(gameAI)

GAME_UPDATE = pygame.USEREVENT
GAME_SPEED = 200
pygame.time.set_timer(GAME_UPDATE, GAME_SPEED)
added = False

paused = False

while True:
    elapsed_time = time.time() - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if gamePlayer.game_over:
                added = False
                gamePlayer.game_over = False
                gamePlayer.reset()
                gameAI.game_over = False
                gameAI.reset()
            if event.key == pygame.K_LEFT and not gamePlayer.game_over:
                gamePlayer.move_left()
            if event.key == pygame.K_RIGHT and not gamePlayer.game_over:
                gamePlayer.move_right()
            if event.key == pygame.K_DOWN and not gamePlayer.game_over:
                gamePlayer.move_down()
            gamePlayer.update_score(0, 1)
            if event.key == pygame.K_UP and not gamePlayer.game_over:
                gamePlayer.rotate()
            if event.key == pygame.K_SPACE and not gamePlayer.game_over:
                gamePlayer.drop_block()
            if event.key == pygame.K_p:
                paused = not paused  # Toggle pause state
        if event.type == GAME_UPDATE and not gamePlayer.game_over and not paused:
            gamePlayer.move_down()
        if not gameAI.game_over and not paused:
            tetris_ai.make_best_move()
            gameAI.update()

    # Continue with game logic
    current_piece = gamePlayer.current_block
    next_piece = gamePlayer.next_block
    score_value_surface = title_font.render(str(gamePlayer.score), True, Colors.white)
    score_value_surface_ai = title_font.render(str(gameAI.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    #player 1
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    #player2
    screen.blit(score_surface, (860, 20, 50, 50))
    screen.blit(next_surface, (870, 180, 50, 50))

    if gamePlayer.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))
    elif paused:
        screen.blit(paused_surface, (350, 450, 50, 50))

    if gameAI.game_over:
        screen.blit(game_over_surface, (820, 450, 50, 50))
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")

        # Your existing code to check if data is added
        if not added:
            with open(file_path, "a") as f:
                f.write("----------------------------------------" +
                        "\nHeight: " + str(tetris_ai.height_multiplier) +
                        "\nLines : " + str(tetris_ai.lines_cleared_multiplier) +
                        "\nHoles : " + str(tetris_ai.holes_multiplier) +
                        "\nBumps : " + str(tetris_ai.bumpiness_multiplier) +
                        "\nScore :" + str(gameAI.score) +
                        "\n----------------------------------------\n")
                added = True
    elif paused:
        screen.blit(paused_surface, (850, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface,
                score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, score_rect2, 0, 10)
    screen.blit(score_value_surface_ai,
            score_value_surface_ai.get_rect(centerx=score_rect2.centerx, centery=score_rect2.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, next_rect2, 0, 10)
    gamePlayer.draw(screen, x_offset=0)
    gameAI.draw(screen, x_offset=500)

    pygame.display.update()
    clock.tick(60)
