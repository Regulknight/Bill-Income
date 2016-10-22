class Player:
    money = 0
    income_source = []

    def __init__(self):


    def get_income(self):
        for inc_s in self.income_source:
            if inc_s.get_t <= 0:
                self.money += inc_s.get_inc()
                inc_s.refresh()

    def buy_income_source(self, i, n):
        if self.income_source[i].get_price(n) * n <= self.money:





