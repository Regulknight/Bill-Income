import time
import pygame

from Income_source import IncomeSource
from Player import Player
import os


# Загрузка данных об источниках доходов
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


# Загрузка настроек игры
def load_settings():
    f = open("settings.txt", 'r')
    str = f.readline()
    width = int(str.split(' ')[1])
    height = int(str.split(' ')[2])
    return width, height


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

def print_msg(str, size, color, backcolor, coord):
    fontObj = pygame.font.Font('Mono.ttf', size)
    textSurfaceObj = fontObj.render(str, True, color, backcolor)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.midleft = (150, 225)
    screen.blit(textSurfaceObj, textRectObj)


income_sources = load_income_source("Sorce_of_income_data.txt")
player = Player(income_sources)
screen = screen.set_mode(load_settings())

while True:
    print_msg("Capital: " + '%.2f' % player.money + " R", 30, (255, 255, 255), (0, 0, 0), (150, 240))
    player.tick(0.1)
    time.sleep(0.1)
    pygame.display.flip()


