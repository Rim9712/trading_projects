import pandas as pd
import yfinance as yf
import pandas_ta as ta

def get_stock_data(tickers:list, start_date, end_date) -> pd.DataFrame: 
        """
        Get stock historical data 
        """
        # Ensuring dates are in string format compatible with yfinance
        start_date_e = pd.to_datetime(start_date, format = '%Y/%m/%d')
        end_date_e = pd.to_datetime(end_date, format = '%Y/%m/%d')

        # Fetch data using adjusted dates
        data = []
        for ticker in tickers: 
            try:
                df= yf.download(ticker,start = start_date_e, end = end_date_e)
                df.columns = [f'{col}' for col in df.columns]
                data.append(df)
                print(f"Succesfully downloaded {ticker}")
            except Exception as e:
                print(f"Error downloading {ticker}:{e}")
                return None
        combined_df = pd.concat(data, axis=1)
        return combined_df
        
def save_data(data: pd.DataFrame, filename: str):
        """
        Save data to csv 
        """
        data.to_csv(f"{filename}.csv")


df = get_stock_data(['AAPL', 'MSFT', 'GOOGL'], "2020/01/01","2024/01/01")
save_data(df, "Apple data")


