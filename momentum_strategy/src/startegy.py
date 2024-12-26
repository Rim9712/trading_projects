import pandas as pd
import yfinance as yf
import pandas_ta as ta

def get_stock_data(symbol, start_date, end_date) -> pd.DataFrame: 
        """
        Get stock historical data 
        """
        try:
            # Ensuring dates are in string format compatible with yfinance
            start_date_e = pd.to_datetime(start_date, format = '%Y/%m/%d')
            end_date_e = pd.to_datetime(end_date, format = '%Y/%m/%d')
            
            # Fetch data using adjusted dates
            data = yf.download(symbol,start = start_date_e, end = end_date_e)
            return data
        
        except Exception as e:
            print(f"Error downloading{symbol}:{e}")
            return None

def save_data(data: pd.DataFrame, filename: str):
        """
        Save data to csv 
        """
        data.to_csv(f"{filename}.csv")


df = get_stock_data('AAPL', "2020/01/01","2024/01/01")
save_data(df, "Apple data")


