Statistical Arbitrage / Pairs trading backtest

Progression across the notebooks:
1. naive baseline - fixed threshold mean-reversion, on just price spread (ratio)

2. cointegration-based pair selection - get a wide universe of stocks in different sectors, pair them all up,
run a cointegration test on them to see whether they are cointegrated, then run OLS regression in order to get 
parameters like hedge ratio and spread, then same as notebook 1.

3. dynamic hedge ratio - beta changing constantly throughout time frame models true market movement better as
in reality it would not stay constant.

4. portfolio + risk controls - increasing portfolio allows for a test on whether the strategy was just a one off
for one sole pair, or works over generalised stock pairs that follow similar trends. risk controls also allow 
for better management as we can introduce limits to which money loss can be prevented, and to only trade whithin
bounds deemed safe.

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


3. using the kalman filter allowed a dynamic hedge ratio instead of static one. this follows true market trends more closely
as the hedge ratio between the two wouldnt stay the same due to a variety of reasons. on the kalman filter model, beta swung 
quite a lot in the early months of the time frame, so in order to have a fair comparison of when it was settling down around
an average i removed / only looked from when it was stable. i then re-ran the previous model, with the static hedge ratio
over the same time frame, and compared the results of each, which are:

Cointegration-based Sharpe (SAM/BF-B): 1.23
Total P&L (spread units): 160.14
Number of trades: 21

Kalman-based Sharpe (SAM/BF-B): 1.77
Total P&L (spread units): 164.63
Number of trades: 21

here we can see that introducing the kalman filter increased the sharpe ratio by a good amount, however must take note of the 
fact there were only 21 trades so not a very big sample size to draw this conclusion on. the p&l being very similar though 
does tell us that the use of this dynamic beta allowed for a return of similar money, but with less volatility. the same 
trades also demonstrate that improvement isnt coming from trading more or less, just from the increase in quality of the spread

4. in introducing a portfolio of the top 4 stock pairs, which were determined from notebook 2s screening of best statistics / 
lowest p values, there were a few interesting results. first of all, SAM BF-B was checked with the new windows and walk-forward
model, before introducing more pairs to it, which gave us the following:

0  2022-01-01 2023-01-01 2023-01-01 2023-04-01  0.020945    True
1  2022-04-01 2023-04-01 2023-04-01 2023-07-01  0.052710   False
2  2022-07-01 2023-07-01 2023-07-01 2023-10-01  0.082072   False
3  2022-10-01 2023-10-01 2023-10-01 2024-01-01  0.323046   False
Windows traded: 1 / 4
Walk-forward out-of-sample Sharpe (SAM/BF-B): 3.69   

here we can see that by testing for cointegration across each window, instead of just leaving it as one test, the last 3 windows
didnt pass the test, so were skipped of any trades. this explicitly shows the two stocks drifted apart and were not following 
similar trends. for the one traded period the sharpe was quite high at 3.69, however for such a small period this needs to be 
interpreted carefully, as it could have just been a lucky time. 

when introducing the other pairs we get the following full portfolio statistics:

Portfolio walk-forward Sharpe: 1.98
Portfolio max drawdown: -8.02
COP/EOG: walk-forward Sharpe = 0.48
BAC/PNC: never traded (failed cointegration in every walk-forward window)
SAM/BF-B: walk-forward Sharpe = 3.69
INTC/MU: walk-forward Sharpe = -1.17


the overall portfolio sharpe ratio is quite good at 1.98, however again not over a massive period of time and the SAM/BF-B does 
help it a lot. 0.48 for COP/EOG is a moderate one, showing good returns, and the INTC/MU  = -1.17 is showing that even though 
two of the stocks may be correlated, this particular trading strategy isnt perfect. the risk controls also are shown to work 
as required with BAC/PNC, as in all 4 windows it never passed the cointegration test, therefore never was allowed to trade.
