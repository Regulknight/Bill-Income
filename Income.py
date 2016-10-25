def buy_bill():
    global count_of_Bills
    global count_of_money
    if count_of_money > 62000:
        count_of_money -= 62000
        count_of_Bills += 1


income_per_millisec = 60.83


while game_cycle:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_x:
                buy_bill()
            if event.key == pg.K_ESCAPE:
                game_cycle = False


