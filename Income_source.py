class IncomeSource:
    income = 0.0
    time = 0.0
    name = "unnamed"
    t = time
    count_of_income_source = 0
    price = 0
    n_limit = 0

    def __init__(self, inc, t, name, count, n):
        self.income = inc
        self.time = t
        self.name = name
        self.count_of_income_source = count
        self.n_limit = n

    def get_inc(self):
        return  self.income

    def refresh(self):
        self.t = self.time

    def tick(self, tick_time):
        self.t -= tick_time

    def buy_income_source(self, n):
        self.count_of_income_source += n

    def get_price(self, n):
        price = 0
        for i in range(0, n):
            price += self.price * ((self.count_of_income_source + i) * 0.1 + 1)
        return price





