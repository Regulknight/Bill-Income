import time
import pygame
from Income_source import IncomeSource
from Player import Player
from Settings import Settings

settings = Settings()
settings.load_settings()


def load_income_source(filename):
    income_sources = []
    f = open(filename, 'r')
    for str in f:
        i_s = str.split(' ')
        name = i_s[0]
        inc = float(i_s[1])
        t = float(i_s[2])
        count = float(i_s[3])
        price = float(i_s[4])
        n = float(i_s[5])
        income_source = IncomeSource(name, inc, t, count, price, n)
        income_sources.append(income_source)
    return income_sources


def display(i_s):
    for i in i_s:
        print(i.name)
        print(i.income)
        print(i.time)
        print(i.t)
        print(i.count_of_income_source)
        print(i.price)
        print(i.n_limit)
        print()

pygame.init()
screen = pygame.display


def print_msg(msg, size, color, back_color, coord, font="Mono.ttf"):
    font_obj = pygame.font.Font(font, size)
    text_surface_obj = font_obj.render(msg, True, color, back_color)
    text_react_obj = text_surface_obj.get_rect()
    text_react_obj.midleft = coord
    screen.blit(text_surface_obj, text_react_obj)


def show_progress(progress_list):
    i = 0
    for progress in progress_list:
        print_msg(str(progress), 15, (255, 255, 255), (0, 0, 0), (200, 10 + i*30))
        i += 1


def show_prices(price_list, n):
    i = 0
    for price in price_list:
        print_msg(str(round(price, 2)) + " x" + str(n), 15, (255, 255, 255), (0, 0, 0), (250, 10 + i*30))
        i += 1


def show_names(name_list):
    i = 0
    for name in name_list:
        print_msg(name + ": ", 15, (255, 255, 255), (0, 0, 0), (0, 10 + i * 30))
        i += 1


def show_count_of_income(count_list):
    i = 0
    for count in count_list:
        print_msg(str(count), 15, (255, 255, 255), (0, 0, 0), (150, 10 + i * 30))
        i += 1

income_sources = load_income_source("Source_of_income_data.txt")
player = Player(income_sources)
screen = screen.set_mode((settings.screen_width, settings.screen_height))
if settings.full_screen:
    pygame.display.toggle_fullscreen()
game_cycle = True

while game_cycle:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_cycle = False

    print_msg("Capital: " + '%.2f' % player.money + " R", 30, (255, 255, 255), (0, 0, 0), (150, 240))
    player.tick(0.1)
    time.sleep(0.1)
    show_progress(player.get_progress_list())
    show_prices(player.get_price_list(1), 1)
    show_names(player.get_names_list())
    show_count_of_income(player.get_count_list())
    pygame.display.flip()

