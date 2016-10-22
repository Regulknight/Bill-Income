import time
import os
import pygame as pg

game_cycle = True
count_of_Bills = 1
count_of_money = 0

def buy_bill():
    global count_of_Bills
    global count_of_money
    if count_of_money > 62000:
        count_of_money -= 62000
        count_of_Bills += 1


income_per_millisec = 60.83

pg.init()
screen = pg.display.set_mode((640, 480))


i = 0
while game_cycle:

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_x:
                buy_bill()
            if event.key == pg.K_ESCAPE:
                game_cycle = False

    count_of_money += income_per_millisec * count_of_Bills

    time.sleep(0.01)
    screen.fill((0, 0, 0))

    fontObj = pg.font.Font('Mono.ttf', 30)

    textSurfaceObj = fontObj.render("Capital: " + '%.2f' % (count_of_money) + " R", True, (255, 255, 255), (0, 0, 0))
    textSurfaceObj_z = fontObj.render("Count of Bills: " + str(count_of_Bills), True, (255, 0 , 255), (0, 0, 0))
    textRectObj_z = textSurfaceObj_z.get_rect()
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.midleft = (150, 225)
    textRectObj_z.midleft = (150, 255)
    screen.blit(textSurfaceObj_z, textRectObj_z)
    screen.blit(textSurfaceObj, textRectObj)
    pg.display.flip()
