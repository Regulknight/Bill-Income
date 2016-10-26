from Income_source import IncomeSource

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


class Player:
    money = 0
    income_sources = []

    def __init__(self, path="Source_of_income_data.txt"):

        self.income_sources = load_income_source(path)
        self.money = 0

    def get_income(self, i_s):
        self.money = self.money + i_s.get_income()

    def buy_income_source(self, i, n):
        if self.income_source[i].get_price(n) <= self.money:
            self.money -= self.income_sources[i].get_price(n)
            self.income_sources[i].buy_income_source(n)

    def tick(self, t):
        for i in self.income_sources:
            if i.count_of_income_source != 0:
                if i.tick(t):
                    self.get_income(i)

    def get_progress_list(self):
        progress_list = []
        for i_s in self.income_sources:
            progress_list.append(round(i_s.t/i_s.time, 2))
        return progress_list

    def get_price_list(self, n):
        price_list = []
        for i_s in self.income_sources:
            price_list.append(i_s.get_price(n))
        return price_list

    def get_names_list(self):
        name_list = []
        for i_s in self.income_sources:
            name_list.append(i_s.name)
        return name_list

    def get_count_list(self):
        count_list = []
        for i_s in self.income_sources:
            count_list.append(i_s.count_of_income_source)
        return count_list





