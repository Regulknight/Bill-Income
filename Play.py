import time
import pygame
from Game import Game

pygame.init()
game = Game()
game_cycle = True

while game_cycle:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_cycle = False

    game.print_msg("Capital: " + '%.2f' % game.player.money + " R", 30, (255, 255, 255), (0, 0, 0), (150, 240))
    game.player.tick(0.1)
    time.sleep(0.1)
    game.show_all()
    pygame.display.flip()

