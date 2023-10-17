from generate_dataset import stock_data
from portfolio import Portfolio


# this is a trading bot script with the moving average crossover algorithm implemented



def generate_signals(df):

    x = 10
    y = 50

    # kalkulerer short (x-dager) og long (y-dager) moving average
    df['Short_MA'] = df['Close_Upward_Trend'].rolling(window=x).mean()
    df['Long_MA'] = df['Close_Upward_Trend'].rolling(window=y).mean()


    df['Signal'] = 0.0
    df.loc[df['Short_MA'] > df['Long_MA'], 'Signal'] = 1.0 # BUY
    df.loc[df['Short_MA'] <= df['Long_MA'], 'Signal'] = -1.0  # SELL

    return df







        


def trade(df, portfolio):

    buying_amount = 1

    set = 'Close_Upward_Trend'

    for i in range(len(df['Signal'])):

        try: 
            price = df[set].iloc[i]
            signal = df['Signal'].iloc[i]

            if signal == 1.0:
                portfolio.buy(price, buying_amount)  # Buying 1 stock
            elif signal == -1.0:
                portfolio.sell(price, buying_amount)  # Selling 1 stock

            # print(f'Final balance: {portfolio.get_balance()} with {portfolio.get_stockamount()} stocks.')


        except ValueError:
            print("ValueError occurred!")
            continue
    

    #sell all stock at the end
    portfolio.sell(df[set].iloc[-1], portfolio.get_stockamount())

    print(f'Final balance: {portfolio.get_balance()} with {portfolio.get_stockamount()} stocks.')


# testing the algo and portfolio interactions


df = generate_signals(stock_data)

p = Portfolio(10000)

trade(df, p)