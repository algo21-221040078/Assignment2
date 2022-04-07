# Assignment2: Fama-French 3-factors
## 1. Introduction
Fama and French(1993) identifies five common risk factors in the returns on stocks 
and bonds in the paper. There are three stock-market factors: an overall market 
factor and factors related to firm size and book-to-market equity.

This paper conducts the asset-pricing tests, using the time-series regression approach
 of Black, Jensen, and Scholes(1972). 

The main results are: For stocks, portfolios constructed to mimic risk factors related to 
size and BE/ME capture strong common variation in returns, no matter what else is in the time-
series regression. The intercepts from three-factor regressions that include the excess market 
return and the mimicking returns for size and BE/ME factors are close to 0.
## 2. Empirical Test
### 2.1 Environment
1. Language: Python 3.7
2. Package: pandas, numpy, datetime, os, statsmodels

### 2.1 Data
We used the historical data of the Shanghai Stock Exchange 50 constituent stocks from February 
1, 2021 to March 1, 2022. At the same time, the factor data in this interval were downloaded from 
the database.

There are 2 data files:  
1. sz50.csv: historical data of the Shanghai Stock Exchange 50 constituent stocks from February 1, 2021 to March 1, 2022.
   (Data Source: WIND)
2. fivefactor_daily: factors data.(Data Source: https://sf.cufe.edu.cn/info/1198/11508.htm)

### 2.2 Model



