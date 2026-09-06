# file to keep previous functions in notebook one the same and reuse in notebook two
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# rolling z score of the spread

def compute_zscore(spread: pd.Series, window: int = 30) -> pd.Series:
    mean = spread.rolling(window=window).mean()
    std = spread.rolling(window=window).std()
    return (spread - mean) / std
# signals
def generate_signals(zscore: pd.Series, entry_threshold: float = 2.0, exit_threshold: float = 0.5) -> pd.Series:
    position = [] # starting position flat = 0, long = 1, short = -1
    current_position = 0  # Initialize current position
    for i in range(0, len(zscore)):
        if current_position == 0: # no position
            if zscore.iloc[i] > entry_threshold:
                current_position = -1  # short the spread

            elif zscore.iloc[i] < -entry_threshold:
                current_position = 1  # long the spread

            else:
                current_position = 0  # maintain no position

        elif current_position == 1: # currently long
            if abs(zscore.iloc[i]) < exit_threshold:
                current_position = 0  # close the position

            else:
                current_position = 1  # maintain the long position

        elif current_position == -1: # currently short
            if abs(zscore.iloc[i]) < exit_threshold:
                current_position = 0  # close the position

            else:
                current_position = -1  # maintain the short position

        position.append(current_position)  # record the current position
    return pd.Series(position, index=zscore.index)

# backtest 
def backtest(positions: pd.Series, spread: pd.Series) -> pd.Series:
    return positions.shift(1) * spread.diff()
# sharpe ratio
def sharpe_ratio(daily_pnl: pd.Series, periods_per_year: int = 252) -> float:
    # assuming risk free rate - annualized Sharpe ratio = (mean daily return / std daily return) * sqrt(periods per year)
    mean_daily_return = daily_pnl.mean()
    std_daily_return = daily_pnl.std()
    return (mean_daily_return / std_daily_return) * np.sqrt(periods_per_year)