import time

from Income_source import IncomeSource
from Player import Player
import os

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


income_sources = load_income_source("Sorce_of_income_data.txt")
player = Player(income_sources)
while True:
    print(player.money)
    player.tick(0.1)
    time.sleep(0.1)
    os.system('clear')

