import pandas as pd

class Dataset:
    def __init__(self):
        self.data = pd.DataFrame()

    def load_data(self, data):
        # For simplicity, assume data is a dict or DataFrame. 
        # In a real-world scenario, this could be an API call.
        self.data = pd.DataFrame(data)
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)
        
    def get_data(self):
        return self.data