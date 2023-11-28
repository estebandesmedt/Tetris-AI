import pygame, sys
import os
import time
from game import Game
from colors import Colors
from tetrisai import TetrisAI
from grid import Grid

pygame.init()
start_time = time.time()

#only 20 and 30 are valid values (20 will be 10 grids, while 30 is 3 grids)
custom_cell_size = 20
ratio = custom_cell_size/30

title_font = pygame.font.Font(None, round(ratio*40))
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
paused_surface = title_font.render("PAUSED", True, Colors.white)

# player 1 top
score_rect = pygame.Rect(ratio*320, ratio*55, ratio*170, ratio*60)
next_rect = pygame.Rect(ratio*320, ratio*215, ratio*170, ratio*180)
# player 2 top
score_rect2 = pygame.Rect(ratio*820, ratio*55, ratio*170, ratio*60)
next_rect2 = pygame.Rect(ratio*820, ratio*215, ratio*170, ratio*180)
# player 3 top
score_rect3 = pygame.Rect(ratio*1320, ratio*55, ratio*170, ratio*60)
next_rect3 = pygame.Rect(ratio*1320, ratio*215, ratio*170, ratio*180)

if custom_cell_size != 30:
    # player 4 top
    score_rect4 = pygame.Rect(ratio*1820, ratio*55, ratio*170, ratio*60)
    next_rect4 = pygame.Rect(ratio*1820, ratio*215, ratio*170, ratio*180)
    # player 5 top
    score_rect5 = pygame.Rect(ratio*2320, ratio*55, ratio*170, ratio*60)
    next_rect5 = pygame.Rect(ratio*2320, ratio*215, ratio*170, ratio*180)

    # player 6 bottom
    score_rect6 = pygame.Rect(ratio*320, ratio*755, ratio*170, ratio*60)
    next_rect6 = pygame.Rect(ratio*320, ratio*915, ratio*170, ratio*180)
    # player 7 bottom
    score_rect7 = pygame.Rect(ratio*820, ratio*755, ratio*170, ratio*60)
    next_rect7 = pygame.Rect(ratio*820, ratio*915, ratio*170, ratio*180)
    # player 8 bottom
    score_rect8 = pygame.Rect(ratio*1320, ratio*755, ratio*170, ratio*60)
    next_rect8 = pygame.Rect(ratio*1320, ratio*915, ratio*170, ratio*180)
    # player 9 bottom
    score_rect9 = pygame.Rect(ratio*1820, ratio*755, ratio*170, ratio*60)
    next_rect9 = pygame.Rect(ratio*1820, ratio*915, ratio*170, ratio*180)
    # player 10 bottom
    score_rect10 = pygame.Rect(ratio*2320, ratio*755, ratio*170, ratio*60)
    next_rect10 = pygame.Rect(ratio*2320, ratio*915, ratio*170, ratio*180)


if custom_cell_size != 30:
    screen = pygame.display.set_mode((1675, 900))
else:
    screen = pygame.display.set_mode((1500, 625))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()


gameAI1 = Game(cell_size=custom_cell_size)
gameAI2 = Game(cell_size=custom_cell_size)
gameAI3 = Game(cell_size=custom_cell_size)
if custom_cell_size != 30:
    gameAI4 = Game(cell_size=custom_cell_size)
    gameAI5 = Game(cell_size=custom_cell_size)
    gameAI6 = Game(cell_size=custom_cell_size)
    gameAI7 = Game(cell_size=custom_cell_size)
    gameAI8 = Game(cell_size=custom_cell_size)
    gameAI9 = Game(cell_size=custom_cell_size)
    gameAI10 = Game(cell_size=custom_cell_size)
tetris_ai1 = TetrisAI(gameAI1)  
tetris_ai2 = TetrisAI(gameAI2)  
tetris_ai3 = TetrisAI(gameAI3) 
if custom_cell_size != 30:
    tetris_ai4 = TetrisAI(gameAI4)  
    tetris_ai5 = TetrisAI(gameAI5)  
    tetris_ai6 = TetrisAI(gameAI6) 
    tetris_ai7 = TetrisAI(gameAI7)  
    tetris_ai8 = TetrisAI(gameAI8)  
    tetris_ai9 = TetrisAI(gameAI9) 
    tetris_ai10 = TetrisAI(gameAI10) 

GAME_UPDATE = pygame.USEREVENT
GAME_SPEED = 200
pygame.time.set_timer(GAME_UPDATE, GAME_SPEED)
added1 = False
added2 = False
added3 = False
added4 = False
added5 = False
added6 = False
added7 = False
added8 = False
added9 = False
added10 = False

paused = False
RESTART_DELAY = 3
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
p = 0
q = 0
r = 0
s = 0

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
        if custom_cell_size != 30:
            if event.type == GAME_UPDATE and not gameAI4.game_over and not paused:
                gameAI4.move_down()
            if event.type == GAME_UPDATE and not gameAI5.game_over and not paused:
                gameAI5.move_down()
            if event.type == GAME_UPDATE and not gameAI6.game_over and not paused:
                gameAI6.move_down()
            if event.type == GAME_UPDATE and not gameAI7.game_over and not paused:
                gameAI7.move_down()
            if event.type == GAME_UPDATE and not gameAI8.game_over and not paused:
                gameAI8.move_down()
            if event.type == GAME_UPDATE and not gameAI9.game_over and not paused:
                gameAI9.move_down()
            if event.type == GAME_UPDATE and not gameAI10.game_over and not paused:
                gameAI10.move_down()

    if not gameAI1.game_over and not paused:
        tetris_ai1.make_best_move()
        gameAI1.update()
    if not gameAI2.game_over and not paused:
        tetris_ai2.make_best_move()
        gameAI2.update()
    if not gameAI3.game_over and not paused:
        tetris_ai3.make_best_move()
        gameAI3.update()
    if custom_cell_size != 30:
        if not gameAI4.game_over and not paused:
            tetris_ai4.make_best_move()
            gameAI4.update()
        if not gameAI5.game_over and not paused:
            tetris_ai5.make_best_move()
            gameAI5.update()
        if not gameAI6.game_over and not paused:
            tetris_ai6.make_best_move()
            gameAI6.update()
        if not gameAI7.game_over and not paused:
            tetris_ai7.make_best_move()
            gameAI7.update()
        if not gameAI8.game_over and not paused:
            tetris_ai8.make_best_move()
            gameAI8.update()
        if not gameAI9.game_over and not paused:
            tetris_ai9.make_best_move()
            gameAI9.update()
        if not gameAI10.game_over and not paused:
            tetris_ai10.make_best_move()
            gameAI10.update()

    # Continue with game logic
    current_piece = gameAI1.current_block
    next_piece = gameAI1.next_block
    score_value_surface = title_font.render(str(gameAI1.score), True, Colors.white)
    score_value_surface_ai = title_font.render(str(gameAI2.score), True, Colors.white)
    score_value_surface_ai3 = title_font.render(str(gameAI3.score), True, Colors.white)
    if custom_cell_size != 30:
        score_value_surface_ai4 = title_font.render(str(gameAI4.score), True, Colors.white)
        score_value_surface_ai5 = title_font.render(str(gameAI5.score), True, Colors.white)
        score_value_surface_ai6 = title_font.render(str(gameAI6.score), True, Colors.white)
        score_value_surface_ai7 = title_font.render(str(gameAI7.score), True, Colors.white)
        score_value_surface_ai8 = title_font.render(str(gameAI8.score), True, Colors.white)
        score_value_surface_ai9 = title_font.render(str(gameAI9.score), True, Colors.white)
        score_value_surface_ai10 = title_font.render(str(gameAI10.score), True, Colors.white)

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
    if custom_cell_size != 30:
        # player 4
        screen.blit(score_surface, (ratio*1860, ratio*20, ratio*50, ratio*50))
        screen.blit(next_surface, (ratio*1875, ratio*180, ratio*50, ratio*50))
        # player 5
        screen.blit(score_surface, (ratio*2365, ratio*20, ratio*50, ratio*50))
        screen.blit(next_surface, (ratio*2375, ratio*180, ratio*50, ratio*50))
        # player 6
        screen.blit(score_surface, (ratio*365, ratio*720, ratio*50, ratio*50))
        screen.blit(next_surface, (ratio*375, ratio*880, ratio*50, ratio*50))
        # player 7
        screen.blit(score_surface, (ratio*860, ratio*720, ratio*50, ratio*50))
        screen.blit(next_surface, (ratio*870, ratio*880, ratio*50, ratio*50))
        # player 8
        screen.blit(score_surface, (ratio*1365, ratio*720, ratio*50, ratio*50))
        screen.blit(next_surface, (ratio*1375, ratio*880, ratio*50, ratio*50))
        # player 9
        screen.blit(score_surface, (ratio*1860, ratio*720, ratio*50, ratio*50))
        screen.blit(next_surface, (ratio*1875, ratio*880, ratio*50, ratio*50))
        # player 10
        screen.blit(score_surface, (ratio*2365, ratio*720, ratio*50, ratio*50))
        screen.blit(next_surface, (ratio*2375, ratio*880, ratio*50, ratio*50))


    if gameAI1.game_over:
        screen.blit(game_over_surface, (ratio*320, ratio*450, ratio*50, ratio*50))
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")
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
        if not added3:
            with open(file_path, "a") as f:
                f.write("----------------------------------------" +
                        "\nHeight: " + str(tetris_ai3.height_multiplier) +
                        "\nLines : " + str(tetris_ai3.lines_cleared_multiplier) +
                        "\nHoles : " + str(tetris_ai3.holes_multiplier) +
                        "\nBumps : " + str(tetris_ai3.bumpiness_multiplier) +
                        "\nScore :" + str(gameAI3.score) +
                        "\n----------------------------------------\n")
                added3 = True
                k += 1
                print(k)
                if k % 10 == 0:
                    tetris_ai3.mutation()
                    print("3\nHeight: " + str(tetris_ai3.height_multiplier) + "\nHoles: "+ str(tetris_ai3.holes_multiplier))
    if custom_cell_size != 30:
        if gameAI4.game_over:
            screen.blit(game_over_surface, (ratio*1820, ratio*450, ratio*50, ratio*50))
            file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")
            if not added4:
                with open(file_path, "a") as f:
                    f.write("----------------------------------------" +
                            "\nHeight: " + str(tetris_ai4.height_multiplier) +
                            "\nLines : " + str(tetris_ai4.lines_cleared_multiplier) +
                            "\nHoles : " + str(tetris_ai4.holes_multiplier) +
                            "\nBumps : " + str(tetris_ai4.bumpiness_multiplier) +
                            "\nScore :" + str(gameAI4.score) +
                            "\n----------------------------------------\n")
                    added4 = True
                    l += 1
                    print(l)
                    if l % 10 == 0:
                        tetris_ai4.mutation()
                        print("4\nHeight: " + str(tetris_ai4.height_multiplier) + "\nHoles: "+ str(tetris_ai4.holes_multiplier))
            if gameAI5.game_over:
                screen.blit(game_over_surface, (ratio*2320, ratio*450, ratio*50, ratio*50))
                file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")
                if not added5:
                    with open(file_path, "a") as f:
                        f.write("----------------------------------------" +
                                "\nHeight: " + str(tetris_ai5.height_multiplier) +
                                "\nLines : " + str(tetris_ai5.lines_cleared_multiplier) +
                                "\nHoles : " + str(tetris_ai5.holes_multiplier) +
                                "\nBumps : " + str(tetris_ai5.bumpiness_multiplier) +
                                "\nScore :" + str(gameAI5.score) +
                                "\n----------------------------------------\n")
                        added5 = True
                        m += 1
                        print(m)
                        if m % 10 == 0:
                            tetris_ai5.mutation()
                            print("5\nHeight: " + str(tetris_ai5.height_multiplier) + "\nHoles: "+ str(tetris_ai5.holes_multiplier))
        if gameAI6.game_over:
            screen.blit(game_over_surface, (ratio*320, ratio*1150, ratio*50, ratio*50))
            file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")
            if not added6:
                with open(file_path, "a") as f:
                    f.write("----------------------------------------" +
                            "\nHeight: " + str(tetris_ai6.height_multiplier) +
                            "\nLines : " + str(tetris_ai6.lines_cleared_multiplier) +
                            "\nHoles : " + str(tetris_ai6.holes_multiplier) +
                            "\nBumps : " + str(tetris_ai6.bumpiness_multiplier) +
                            "\nScore :" + str(gameAI6.score) +
                            "\n----------------------------------------\n")
                    added6 = True
                    n += 1
                    print(n)
                    if n % 10 == 0:
                        tetris_ai6.mutation()
                        print("6\nHeight: " + str(tetris_ai6.height_multiplier) + "\nHoles: "+ str(tetris_ai6.holes_multiplier))
        if gameAI7.game_over:
            screen.blit(game_over_surface, (ratio*820, ratio*1150, ratio*50, ratio*50))
            file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")
            if not added7:
                with open(file_path, "a") as f:
                    f.write("----------------------------------------" +
                            "\nHeight: " + str(tetris_ai7.height_multiplier) +
                            "\nLines : " + str(tetris_ai7.lines_cleared_multiplier) +
                            "\nHoles : " + str(tetris_ai7.holes_multiplier) +
                            "\nBumps : " + str(tetris_ai7.bumpiness_multiplier) +
                            "\nScore :" + str(gameAI7.score) +
                            "\n----------------------------------------\n")
                    added7 = True
                    p += 1
                    print(p)
                    if p % 10 == 0:
                        tetris_ai7.mutation()
                        print("7\nHeight: " + str(tetris_ai7.height_multiplier) + "\nHoles: "+ str(tetris_ai7.holes_multiplier))
        if gameAI8.game_over:
            screen.blit(game_over_surface, (ratio*1320, ratio*1150, ratio*50, ratio*50))
            file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")
            if not added8:
                with open(file_path, "a") as f:
                    f.write("----------------------------------------" +
                            "\nHeight: " + str(tetris_ai8.height_multiplier) +
                            "\nLines : " + str(tetris_ai8.lines_cleared_multiplier) +
                            "\nHoles : " + str(tetris_ai8.holes_multiplier) +
                            "\nBumps : " + str(tetris_ai8.bumpiness_multiplier) +
                            "\nScore :" + str(gameAI8.score) +
                            "\n----------------------------------------\n")
                    added8 = True
                    q += 1
                    print(q)
                    if q % 10 == 0:
                        tetris_ai8.mutation()
                        print("8\nHeight: " + str(tetris_ai8.height_multiplier) + "\nHoles: "+ str(tetris_ai8.holes_multiplier))
        if gameAI9.game_over:
            screen.blit(game_over_surface, (ratio*1820, ratio*1150, ratio*50, ratio*50))
            file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")
            if not added9:
                with open(file_path, "a") as f:
                    f.write("----------------------------------------" +
                            "\nHeight: " + str(tetris_ai9.height_multiplier) +
                            "\nLines : " + str(tetris_ai9.lines_cleared_multiplier) +
                            "\nHoles : " + str(tetris_ai9.holes_multiplier) +
                            "\nBumps : " + str(tetris_ai9.bumpiness_multiplier) +
                            "\nScore :" + str(gameAI9.score) +
                            "\n----------------------------------------\n")
                    added9 = True
                    r += 1
                    print(r)
                    if r % 10 == 0:
                        tetris_ai9.mutation()
                        print("9\nHeight: " + str(tetris_ai9.height_multiplier) + "\nHoles: "+ str(tetris_ai9.holes_multiplier))
            if gameAI10.game_over:
                screen.blit(game_over_surface, (ratio*2320, ratio*1150, ratio*50, ratio*50))
                file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ai_score.txt")
                if not added10:
                    with open(file_path, "a") as f:
                        f.write("----------------------------------------" +
                                "\nHeight: " + str(tetris_ai10.height_multiplier) +
                                "\nLines : " + str(tetris_ai10.lines_cleared_multiplier) +
                                "\nHoles : " + str(tetris_ai10.holes_multiplier) +
                                "\nBumps : " + str(tetris_ai10.bumpiness_multiplier) +
                                "\nScore :" + str(gameAI10.score) +
                                "\n----------------------------------------\n")
                        added10 = True
                        s += 1
                        print(s)
                        if s % 10 == 0:
                            tetris_ai10.mutation()
                            print("10\nHeight: " + str(tetris_ai10.height_multiplier) + "\nHoles: "+ str(tetris_ai10.holes_multiplier))
    if custom_cell_size != 30:
        if gameAI1.game_over and gameAI2.game_over and gameAI3.game_over and gameAI4.game_over and gameAI5.game_over and gameAI6.game_over and gameAI7.game_over and gameAI8.game_over and gameAI9.game_over and gameAI10.game_over:
            screen.blit(game_over_surface, (ratio*320, ratio*450, ratio*50, ratio*50))
            if elapsed_time > RESTART_DELAY:
                gameAI1.game_over = False
                gameAI1.reset()
                gameAI2.game_over = False
                gameAI2.reset()
                gameAI3.game_over = False
                gameAI3.reset()
                gameAI4.game_over = False
                gameAI4.reset()
                gameAI5.game_over = False
                gameAI5.reset()
                gameAI6.game_over = False
                gameAI6.reset()
                gameAI7.game_over = False
                gameAI7.reset()
                gameAI8.game_over = False
                gameAI8.reset()
                gameAI9.game_over = False
                gameAI9.reset()
                gameAI10.game_over = False
                gameAI10.reset()
                start_time = time.time() 
                added1 = False
                added2 = False
                added3 = False
                added4 = False
                added5 = False
                added6 = False
                added7 = False
                added8 = False
                added9 = False
                added10 = False
        elif paused:
            screen.blit(paused_surface, (ratio*350, ratio*450, ratio*50, ratio*50))
    
    if custom_cell_size == 30:
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
    if custom_cell_size != 30:
        pygame.draw.rect(screen, Colors.light_blue, score_rect4, 0, 10)
        screen.blit(score_value_surface_ai4,
                    score_value_surface_ai4.get_rect(centerx=score_rect4.centerx, centery=score_rect4.centery))
        pygame.draw.rect(screen, Colors.light_blue, score_rect5, 0, 10)
        screen.blit(score_value_surface_ai5,
                        score_value_surface_ai5.get_rect(centerx=score_rect5.centerx, centery=score_rect5.centery))
        pygame.draw.rect(screen, Colors.light_blue, score_rect6, 0, 10)
        screen.blit(score_value_surface_ai6,
                    score_value_surface_ai6.get_rect(centerx=score_rect6.centerx, centery=score_rect6.centery))
        pygame.draw.rect(screen, Colors.light_blue, score_rect7, 0, 10)
        screen.blit(score_value_surface_ai7,
                    score_value_surface_ai7.get_rect(centerx=score_rect7.centerx, centery=score_rect7.centery))
        pygame.draw.rect(screen, Colors.light_blue, score_rect8, 0, 10)
        screen.blit(score_value_surface_ai8,
                    score_value_surface_ai8.get_rect(centerx=score_rect8.centerx, centery=score_rect8.centery))
        pygame.draw.rect(screen, Colors.light_blue, score_rect9, 0, 10)
        screen.blit(score_value_surface_ai9,
                    score_value_surface_ai9.get_rect(centerx=score_rect9.centerx, centery=score_rect9.centery))
        pygame.draw.rect(screen, Colors.light_blue, score_rect10, 0, 10)
        screen.blit(score_value_surface_ai10,
                    score_value_surface_ai10.get_rect(centerx=score_rect10.centerx, centery=score_rect10.centery))
    
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, next_rect2, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, next_rect3, 0, 10)
    if custom_cell_size != 30:
        pygame.draw.rect(screen, Colors.light_blue, next_rect4, 0, 10)
        pygame.draw.rect(screen, Colors.light_blue, next_rect5, 0, 10)
        pygame.draw.rect(screen, Colors.light_blue, next_rect6, 0, 10)
        pygame.draw.rect(screen, Colors.light_blue, next_rect7, 0, 10)
        pygame.draw.rect(screen, Colors.light_blue, next_rect8, 0, 10)
        pygame.draw.rect(screen, Colors.light_blue, next_rect9, 0, 10)
        pygame.draw.rect(screen, Colors.light_blue, next_rect10, 0, 10)

    gameAI1.draw(screen, x_offset=ratio*0, custom_cell_size=custom_cell_size, ratio=ratio)
    gameAI2.draw(screen, x_offset=ratio*500, custom_cell_size=custom_cell_size, ratio=ratio)
    gameAI3.draw(screen, x_offset=ratio*1000, custom_cell_size=custom_cell_size, ratio=ratio)
    if custom_cell_size != 30:
        gameAI4.draw(screen, x_offset=ratio*1500, custom_cell_size=custom_cell_size, ratio=ratio)
        gameAI5.draw(screen, x_offset=ratio*2000, custom_cell_size=custom_cell_size, ratio=ratio)
        gameAI6.draw(screen, x_offset=ratio*0, y_offset=475, custom_cell_size=custom_cell_size, ratio=ratio)
        gameAI7.draw(screen, x_offset=ratio*500, y_offset=475 , custom_cell_size=custom_cell_size, ratio=ratio)
        gameAI8.draw(screen, x_offset=ratio*1000, y_offset=475 , custom_cell_size=custom_cell_size, ratio=ratio)
        gameAI9.draw(screen, x_offset=ratio*1500, y_offset=475 , custom_cell_size=custom_cell_size, ratio=ratio)
        gameAI10.draw(screen, x_offset=ratio*2000, y_offset=475 , custom_cell_size=custom_cell_size, ratio=ratio)

    pygame.display.update()
    clock.tick(60)