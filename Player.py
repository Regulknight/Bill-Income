

class Player:
    money = 0
    income_source = []

    def __init__(self, i_s):
        self.income_source = i_s
        self.money = 0

    def get_income(self, i_s):
        self.money = self.money + i_s.get_income()

#    def buy_income_source(self, i, n):
#        if self.income_source[i].get_price(n) * n <= self.money:

    def tick(self, t):
        for i in self.income_source:
            if i.count_of_income_source != 0:
                if i.tick(t):
                    self.get_income(i)








