import pandas as pd

# Mock data retrieval function. In reality, this would interface with an API.


# Denne funksjonen returnerer en dataFrame av dataene 
def get_historical_data():
    # Here we're simulating a dataframe with Date, Open, High, Low, Close, Volume columns
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'Open': [100, 101, 102, 103, 102],
        'High': [105, 106, 107, 108, 107],
        'Low': [99, 98, 97, 96, 95],
        'Close': [104, 103, 104, 105, 104],
        'Volume': [1000, 1100, 1200, 1300, 1400]
    }


    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df



def generate_signals(df):
    # Calculate short and long moving averages
    df['Short_MA'] = df['Close'].rolling(window=2).mean()
    df['Long_MA'] = df['Close'].rolling(window=4).mean()
    
    # Generate buy/sell signals
    df['Signal'] = 0.0
    df.loc[df['Short_MA'] > df['Long_MA'], 'Signal'] = 1.0  # Buy Signal
    df.loc[df['Short_MA'] <= df['Long_MA'], 'Signal'] = -1.0  # Sell Signal
    return df




def execute_trade(signal):
    if signal == 1.0:
        print("Executing Buy Order!")
    elif signal == -1.0:
        print("Executing Sell Order!")
    else:
        print("No Trade")


# Main flow
df = get_historical_data()
df = generate_signals(df)

# For this example, let's just act on the last signal
# latest_signal = df['Signal'].iloc[-1]
# execute_trade(latest_signal)

print(get_historical_data())
print('')
print(generate_signals(df))