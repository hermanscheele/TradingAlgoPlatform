from generate_dataset import stock_data




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



def buy(price, balance):

    b = balance
    b -= price
    return b


def sell(price, balance):
    
    b = balance
    b += price
    return b




def execute_trade(signal):
    if signal == 1.0:
        print("BUY")
    elif signal == -1.0:
        print("SELL")
    else:
        print("NO TRADE")

        



df = generate_signals(stock_data)




def trade_on_upward(df, balance):

    set = 'Close_Upward_Trend'
    new_balance = balance

    for i in range(len(df['Signal'])):

        price = df[set].iloc[i]
        signal = df['Signal'].iloc[i]


        if signal == 1.0:
            new_balance = buy(price,new_balance)
            
        elif signal == -1.0:
            new_balance = sell(price,new_balance)

    
    print(f'Original balance: {balance}. New balance: {new_balance}')
            

def trade_on_downward(df, balance):

    set = 'Close_Downward_Trend'
    new_balance = balance

    for i in range(len(df['Signal'])):

        price = df[set].iloc[i]
        signal = df['Signal'].iloc[i]


        if signal == 1.0:
            new_balance = buy(price,new_balance)
            
        elif signal == -1.0:
            new_balance = sell(price,new_balance)

    
    print(f'Original balance: {balance}. New balance: {new_balance}')
            


print(trade_on_upward(df,100000))







