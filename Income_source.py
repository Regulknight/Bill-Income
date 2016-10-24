class IncomeSource:
    income = 0.0
    time = 0.0
    name = "unnamed"
    t = 0
    count_of_income_source = 0
    price = 0
    n_limit = 0

    def __init__(self, name, inc, t, count, price, n):
        self.income = inc
        self.time = t
        self.t = self.time
        self.name = name
        self.count_of_income_source = count
        self.n_limit = n
        self.price = price

    def get_income(self):
        return  self.income*self.count_of_income_source

    def refresh(self):
        self.t = self.time + self.t

    def tick(self, tick_time):
        self.t -= tick_time
        if self.t <= 0:
            self.refresh()
            return True
        return False

    def buy_income_source(self, n):
        self.count_of_income_source += n

    def get_price(self, n):
        price = 0
        for i in range(0, n):
            price += self.price * ((self.count_of_income_source + i) * 0.1 + 1)
        return price





