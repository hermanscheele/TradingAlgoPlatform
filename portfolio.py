import pandas as pd  



class Portfolio:

    def __init__(self, cash):
        self.cash = cash
        self.stockamount = 0


    def buy(self, stockprice, amount):
        self.stockamount += amount
        self.cash -= (amount * stockprice)


    def sell(self, stockprice, amount):

        if (self.stockamount - amount) < 0:
            raise ValueError('Cant sell more stocks than the ones in portfolio')

        self.stockamount -= amount
        self.cash += (amount * stockprice)

        if self.stockamount == 0:
            print('PORTFOLIO NOW EMPTY')
        


    def get_balance(self):
        return self.cash

    def get_stockamount(self):
        return self.stockamount





# data = {'apple': 100, 'IBM': 300}
# port = Portfolio(100, data)


# port.sell('IBM',10,150)

# print(port.get_stocks())


