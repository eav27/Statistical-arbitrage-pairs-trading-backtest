Statistical Arbitrage / Pairs trading backtest

Progression across the notebooks:
1. naive baseline - fixed threshold mean-reversion, on just price spread (ratio)

2. cointegration-based pair selection - 

3. dynamic hedge ratio - 

4. portfolio risk controls - 




NOTES:

1. 
having completed the backtest on a few different stocks i decided were similar / doing the same thing here are results:
(TESLA AND RIVIAN)
Naive baseline Sharpe (TSLA/RIVN): 0.15
Total P&L (spread units): 3.24
Number of trades: 37

(COCA COLA AND PEPSICO)
Naive baseline Sharpe (KO/PEP): -0.39
Total P&L (spread units): -0.03
Number of trades: 38

(EXXONMOBIL AND CHEVRON)
Naive baseline Sharpe (XOM/CVX): 0.10
Total P&L (spread units): 0.02
Number of trades: 43

(SHELL AND BP)
Naive baseline Sharpe (SHEL/BP): 0.59
Total P&L (spread units): 0.27
Number of trades: 52