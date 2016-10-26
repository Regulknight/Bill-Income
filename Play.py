import time
import pygame
from Game import Game
from Button import Button

pygame.init()
game = Game()
game_cycle = True

button1 = Button("McDack_Employee", ((350, 0), (15, 15)), (0, 255, 0))
game.add_button(button1)
button2 = Button("Elon", ((350, 30), (15, 15)), (0, 255, 0))
game.add_button(button2)
button3 = Button("Donald", ((350, 60), (15, 15)), (0, 255, 0))
game.add_button(button3)
button4 = Button("Vladimir", ((350, 90), (15, 15)), (0, 255, 0))
game.add_button(button4)
button5 = Button("Steve", ((350, 120), (15, 15)), (0, 255, 0))
game.add_button(button5)
button6 = Button("Bill", ((350, 150), (15, 15)), (0, 255, 0))
game.add_button(button6)
back = (0,0),(game.settings.screen_width, game.settings.screen_height)

while game_cycle:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_cycle = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in game.buttons:
                if button[0].rect.collidepoint(pygame.mouse.get_pos()):
                    button[0].notify()

    pygame.draw.rect(game.screen, (0,0,0), back)
    game.print_msg("Capital: " + '%.2f' % game.player.money + " R", 30, (255, 255, 255), (0, 0, 0), (150, 240))
    game.player.tick(0.1)
    game.show_all()
    game.draw_buttons()
    pygame.display.update()

