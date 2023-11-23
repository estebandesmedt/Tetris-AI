import pygame, sys
import os
import time
from game import Game
from colors import Colors
from tetrisai import TetrisAI
from grid import Grid

pygame.init()
start_time = time.time()

custom_cell_size = 20
ratio = custom_cell_size/30

title_font = pygame.font.Font(None, round(ratio*40))
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
paused_surface = title_font.render("PAUSED", True, Colors.white)


# player 1
score_rect = pygame.Rect(ratio*320, ratio*55, ratio*170, ratio*60)
next_rect = pygame.Rect(ratio*320, ratio*215, ratio*170, ratio*180)
# player 2
score_rect2 = pygame.Rect(ratio*820, ratio*55, ratio*170, ratio*60)
next_rect2 = pygame.Rect(ratio*820, ratio*215, ratio*170, ratio*180)

score_rect3 = pygame.Rect(ratio*1320, ratio*55, ratio*170, ratio*60)
next_rect3 = pygame.Rect(ratio*1320, ratio*215, ratio*170, ratio*180)

screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()


gameAI1 = Game(cell_size=custom_cell_size)
gameAI2 = Game(cell_size=custom_cell_size)
gameAI3 = Game(cell_size=custom_cell_size)
tetris_ai1 = TetrisAI(gameAI1)  
tetris_ai2 = TetrisAI(gameAI2)  
tetris_ai3 = TetrisAI(gameAI3) 

GAME_UPDATE = pygame.USEREVENT
GAME_SPEED = 200
pygame.time.set_timer(GAME_UPDATE, GAME_SPEED)
added1 = False
added2 = False
added3 = False

paused = False
RESTART_DELAY = 3
i = 0
j = 0
k = 0

while True:
    elapsed_time = time.time() - start_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == GAME_UPDATE and not gameAI1.game_over and not paused:
            gameAI1.move_down()
        if event.type == GAME_UPDATE and not gameAI2.game_over and not paused:
            gameAI2.move_down()
        if event.type == GAME_UPDATE and not gameAI3.game_over and not paused:
            gameAI3.move_down()

    if not gameAI1.game_over and not paused:
        tetris_ai1.make_best_move()
        gameAI1.update()
    if not gameAI2.game_over and not paused:
        tetris_ai2.make_best_move()
        gameAI2.update()
    if not gameAI3.game_over and not paused:
        tetris_ai3.make_best_move()
        gameAI3.update()

    # Continue with game logic
    current_piece = gameAI1.current_block
    next_piece = gameAI1.next_block
    score_value_surface = title_font.render(str(gameAI1.score), True, Colors.white)
    score_value_surface_ai = title_font.render(str(gameAI2.score), True, Colors.white)
    score_value_surface_ai3 = title_font.render(str(gameAI3.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    # player 1
    screen.blit(score_surface, (ratio*365, ratio*20, ratio*50, ratio*50))
    screen.blit(next_surface, (ratio*375, ratio*180, ratio*50, ratio*50))
    # player 2
    screen.blit(score_surface, (ratio*860, ratio*20, ratio*50, ratio*50))
    screen.blit(next_surface, (ratio*870, ratio*180, ratio*50, ratio*50))
    # player 3
    screen.blit(score_surface, (ratio*1365, ratio*20, ratio*50, ratio*50))
    screen.blit(next_surface, (ratio*1375, ratio*180, ratio*50, ratio*50))


    if gameAI1.game_over:
        screen.blit(game_over_surface, (ratio*320, ratio*450, ratio*50, ratio*50))
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")
        # Your existing code to check if data is added
        if not added1:
            with open(file_path, "a") as f:
                f.write("----------------------------------------" +
                        "\nHeight: " + str(tetris_ai1.height_multiplier) +
                        "\nLines : " + str(tetris_ai1.lines_cleared_multiplier) +
                        "\nHoles : " + str(tetris_ai1.holes_multiplier) +
                        "\nBumps : " + str(tetris_ai1.bumpiness_multiplier) +
                        "\nScore :" + str(gameAI1.score) +
                        "\n----------------------------------------\n")
                added1 = True
                j += 1
                print(j)
                if j % 10 == 0:
                    tetris_ai1.mutation()
                    print("1\nHeight: " + str(tetris_ai1.height_multiplier) + "\nHoles: "+ str(tetris_ai1.holes_multiplier))
    if gameAI2.game_over:
        screen.blit(game_over_surface, (ratio*820, ratio*450, ratio*50, ratio*50))
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")
        # Your existing code to check if data is added
        if not added2:
            with open(file_path, "a") as f:
                f.write("----------------------------------------" +
                        "\nHeight: " + str(tetris_ai2.height_multiplier) +
                        "\nLines : " + str(tetris_ai2.lines_cleared_multiplier) +
                        "\nHoles : " + str(tetris_ai2.holes_multiplier) +
                        "\nBumps : " + str(tetris_ai2.bumpiness_multiplier) +
                        "\nScore :" + str(gameAI2.score) +
                        "\n----------------------------------------\n")
                added2 = True
                i += 1
                print(i)
                if i % 10 == 0:
                    tetris_ai2.mutation()
                    print("2\nHeight: " + str(tetris_ai2.height_multiplier) + "\nHoles: "+ str(tetris_ai2.holes_multiplier))
    if gameAI3.game_over:
        screen.blit(game_over_surface, (ratio*1320, ratio*450, ratio*50, ratio*50))
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")
        # Your existing code to check if data is added
        if not added3:
            with open(file_path, "a") as f:
                f.write("----------------------------------------" +
                        "\nHeight: " + str(tetris_ai1.height_multiplier) +
                        "\nLines : " + str(tetris_ai1.lines_cleared_multiplier) +
                        "\nHoles : " + str(tetris_ai1.holes_multiplier) +
                        "\nBumps : " + str(tetris_ai1.bumpiness_multiplier) +
                        "\nScore :" + str(gameAI1.score) +
                        "\n----------------------------------------\n")
                added3 = True
                k += 1
                print(k)
                if k % 10 == 0:
                    tetris_ai3.mutation()
                    print("3\nHeight: " + str(tetris_ai3.height_multiplier) + "\nHoles: "+ str(tetris_ai3.holes_multiplier))

    if gameAI1.game_over and gameAI2.game_over and gameAI3.game_over:
        screen.blit(game_over_surface, (ratio*320, ratio*450, ratio*50, ratio*50))
        if elapsed_time > RESTART_DELAY:
            gameAI1.game_over = False
            gameAI1.reset()
            gameAI2.game_over = False
            gameAI2.reset()
            gameAI3.game_over = False
            gameAI3.reset()
            start_time = time.time() 
            added1 = False
            added2 = False
            added3 = False
    elif paused:
        screen.blit(paused_surface, (ratio*350, ratio*450, ratio*50, ratio*50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface,
                score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, score_rect2, 0, 10)
    screen.blit(score_value_surface_ai,
                score_value_surface_ai.get_rect(centerx=score_rect2.centerx, centery=score_rect2.centery))
    pygame.draw.rect(screen, Colors.light_blue, score_rect3, 0, 10)
    screen.blit(score_value_surface_ai3,
                score_value_surface_ai3.get_rect(centerx=score_rect3.centerx, centery=score_rect3.centery))
    
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, next_rect2, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, next_rect3, 0, 10)

    gameAI1.draw(screen, x_offset=ratio*0)
    gameAI2.draw(screen, x_offset=ratio*500)
    gameAI3.draw(screen, x_offset=ratio*1000)

    pygame.display.update()
    clock.tick(60)
