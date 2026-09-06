Statistical Arbitrage / Pairs trading backtest

Progression across the notebooks:
1. naive baseline - fixed threshold mean-reversion, on just price spread (ratio)

2. cointegration-based pair selection - get a wide universe of stocks in different sectors, pair them all up,
run a cointegration test on them to see whether they are cointegrated, then run OLS regression in order to get 
parameters like hedge ratio and spread, then same as notebook 1.

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


2. having changed the pair selection to something that actually screens them for similarities, we got SAM and BF-B.
this gave us the following statistics:
 ticker_a ticker_b  test_statistics   p_value
0       SAM     BF-B        -4.557746  0.000983.

showed they were strongly correlated, and at a very low p_value indicating that it was not a lucky result they were paired.

using these two tickers for the backtest yielded the following results:
Cointegration-based Sharpe (SAM/BF-B): 1.14
Total P&L (spread units): 234.95
Number of trades: 31

this is compared to:
Naive baseline Sharpe (SAM/BF-B): 0.53
Total P&L (spread units): 2.51
Number of trades: 33

this improved the sharpe and p&l, whilst keeping the number of trades similar, showcasing the benefits of the pair selection.