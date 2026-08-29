# Financial Time-Series Analysis

This folder contains statistical and exploratory analysis of stock and market-index price data developed as part of **MA 374 — Financial Engineering**.

The work focuses on understanding the statistical properties of financial returns across different time scales and evaluating the assumptions underlying classical financial models.

## Topics Covered

- Stock and market-index price analysis
- Daily, weekly, and monthly returns
- Arithmetic and log returns
- Return distributions
- Normalized returns
- Descriptive statistics
- Skewness and kurtosis
- Boxplots and Q-Q plots
- Kolmogorov–Smirnov normality test
- Shapiro–Wilk normality test
- Maximum likelihood estimation
- Confidence intervals
- GBM-based stock-price path simulation
- Comparison of simulated and actual price paths

## Labs

### Lab 06 — Return Analysis & Price Simulation

Analyzed stock and market-index price data from the BSE and NSE datasets across daily, weekly, and monthly time scales.

The analysis includes:

- Plotting stock and index prices against time
- Computing arithmetic returns at daily, weekly, and monthly frequencies
- Constructing normalized-return histograms and comparing them with the standard normal density
- Examining the tails of return distributions
- Comparing arithmetic and log-return behaviour
- Estimating mean return and volatility using log returns
- Generating simulated stock-price paths using the estimated parameters
- Comparing simulated paths with actual stock-price paths across daily, weekly, and monthly frequencies

### Lab 07 — Statistical Analysis of Financial Returns

Extended the return analysis using statistical tools to investigate the distributional properties of financial returns.

The analysis includes:

- Computing mean, standard deviation, skewness, and kurtosis
- Constructing boxplots of returns
- Generating quantile-quantile plots
- Testing the normality assumption using the Kolmogorov–Smirnov test
- Testing the normality assumption using the Shapiro–Wilk test
- Estimating mean and variance using maximum likelihood under a Gaussian assumption
- Computing 95% confidence intervals for the estimated parameters
- Repeating the analysis using log returns
- Extending the analysis to weekly and monthly returns

## Key Concepts

**Price Series → Returns → Distribution Analysis → Normality Testing → Parameter Estimation → Confidence Intervals → GBM Simulation**
