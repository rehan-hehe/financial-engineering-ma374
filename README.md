# MA 374 — Financial Engineering

> **Computational Finance · Derivatives Pricing · Portfolio Theory · Financial Econometrics**

A collection of independently implemented computational finance work completed as part of **MA 374 — Financial Engineering at IIT Guwahati**.

This repository covers the implementation and analysis of financial models using numerical methods, simulation, optimization, and real market data — progressing from **binomial option pricing** and **portfolio optimization** to **Black–Scholes–Merton, implied volatility, Monte Carlo methods, and interest-rate models**.

---

## 📌 What's Inside

| # | Area | Key Topics |
|:---:|---|---|
| **01** | 📈 **Binomial Option Pricing** | European & American options, lookback options, convergence, early exercise, computational efficiency |
| **02** | 💼 **Portfolio Optimization & CAPM** | Markowitz frontier, minimum variance, CML, SML, market portfolio, empirical CAPM |
| **03** | 📊 **Financial Time-Series Analysis** | Returns, distributions, normality tests, statistical estimation, GBM simulation |
| **04** | 🧮 **Black–Scholes–Merton & Volatility** | BSM pricing, parameter sensitivity, historical volatility |
| **05** | 🔎 **Implied Volatility** | Market option data, numerical root finding, volatility surfaces, historical vs implied volatility |
| **06** | 🎲 **Monte Carlo Derivatives Pricing** | GBM simulation, Asian options, risk-neutral pricing, variance reduction |
| **07** | 💰 **Interest Rate Models** | Vasicek, CIR, term structure, yield curves |

---

# 🗂️ Repository Structure

```text
MA374-Financial-Engineering/
│
├── 01_binomial_option_pricing/
│   ├── lab01_european_options/
│   ├── lab02_lookback_options/
│   ├── lab03_american_options/
│   └── README.md
│
├── 02_portfolio_optimization_capm/
│   ├── lab04_markowitz_capm/
│   ├── lab05_no_short_sales_empirical_capm/
│   └── README.md
│
├── 03_financial_time_series/
│   ├── lab06_returns_and_simulation/
│   ├── lab07_statistical_analysis/
│   └── README.md
│
├── 04_bsm_and_volatility/
│   ├── lab08_bsm_pricing/
│   ├── lab09_historical_volatility/
│   └── README.md
│
├── 05_implied_volatility/
│   ├── lab10_implied_vs_historical_volatility/
│   └── README.md
│
├── 06_monte_carlo_pricing/
│   ├── lab11_asian_options/
│   └── README.md
│
├── 07_interest_rate_models/
│   ├── lab12_vasicek_cir/
│   └── README.md
│
├── data/
├── reports/
└── README.md
```

---

# 🧭 Project Overview

## 01 — Binomial Option Pricing

Implemented binomial-tree methods for pricing European, American, and lookback options.

The work includes **backward induction, no-arbitrage checks, convergence analysis, parameter sensitivity, optimal exercise strategies**, and a comparison between basic and computationally efficient Markov-based binomial algorithms.

[→ Explore Binomial Option Pricing](./01_binomial_option_pricing/)

---

## 02 — Portfolio Optimization & CAPM

Applied **Markowitz mean-variance optimization** and **CAPM** to both theoretical and real market data.

The analysis includes **efficient frontiers, minimum-variance portfolios, market portfolios, Capital Market Lines, Security Market Lines, beta estimation**, and empirical analysis using BSE and NSE data.

[→ Explore Portfolio Optimization & CAPM](./02_portfolio_optimization_capm/)

---

## 03 — Financial Time-Series Analysis

Analyzed stock and market-index data at **daily, weekly, and monthly** frequencies.

The work covers **arithmetic and log returns, return distributions, skewness, kurtosis, Q-Q plots, boxplots, Kolmogorov–Smirnov and Shapiro–Wilk normality tests, maximum likelihood estimation**, and GBM-based price-path simulation.

[→ Explore Financial Time-Series Analysis](./03_financial_time_series/)

---

## 04 — Black–Scholes–Merton & Volatility

Implemented the **Black–Scholes–Merton framework** for European call and put options and studied the sensitivity of option prices to model parameters.

Historical volatility was estimated from market data and used for BSM pricing across different strikes and historical estimation windows.

[→ Explore BSM & Volatility](./04_bsm_and_volatility/)

---

## 05 — Implied Volatility & Market Options

Moved from theoretical pricing to **market-observed option prices** for NIFTY and selected stocks.

The analysis includes **option-price surfaces, implied-volatility calculation using numerical root finding, Newton–Raphson iteration, volatility surfaces**, and comparison between historical and implied volatility.

[→ Explore Implied Volatility](./05_implied_volatility/)

---

## 06 — Monte Carlo Derivatives Pricing

Implemented simulation-based derivative pricing using **Geometric Brownian Motion and Monte Carlo methods**.

Asset paths were simulated under both real-world and risk-neutral measures and used to price **arithmetic-average Asian call and put options**. Variance-reduction techniques were subsequently applied and compared.

[→ Explore Monte Carlo Pricing](./06_monte_carlo_pricing/)

---

## 07 — Interest Rate Models

Implemented and analyzed two classical short-rate models:

### Vasicek Model

\[
dr = \beta(\mu-r)\,dt + \sigma\,dW^Q
\]

### CIR Model

\[
dr = \beta(\mu-r)\,dt + \sigma\sqrt{r}\,dW^Q
\]

The analysis focuses on **term structures, yield curves, maturity dependence**, and the effect of different model parameters and initial short rates.

[→ Explore Interest Rate Models](./07_interest_rate_models/)

---

# 🛠️ Computational Methods

The repository brings together several numerical and computational techniques:

- **Binomial tree algorithms**
- **Backward induction**
- **Mean-variance optimization**
- **Statistical estimation**
- **Numerical root finding**
- **Newton–Raphson iteration**
- **Geometric Brownian Motion simulation**
- **Monte Carlo simulation**
- **Variance reduction**
- **Yield-curve computation**
- **2D & 3D visualization**

---

# 📈 From Theory to Computation

The overall progression of the repository can be viewed as:

```text
                    FINANCIAL ENGINEERING
                            │
             ┌──────────────┴──────────────┐
             │                             │
      DERIVATIVE PRICING             PORTFOLIO THEORY
             │                             │
      ┌──────┼────────┐              Markowitz / CAPM
      │      │        │                     │
  Binomial   BSM   Monte Carlo              │
      │      │        │                     │
      │   Implied     │                     │
      │  Volatility   │                     │
      └──────┬────────┘                     │
             │                              │
             └──────────────┬───────────────┘
                            │
                    MARKET DATA ANALYSIS
                            │
                  FINANCIAL TIME SERIES
                            │
                            ▼
                  INTEREST RATE MODELS
                     Vasicek / CIR
```

---

# 🔬 Core Areas

**Quantitative Finance**  
**Derivatives Pricing**  
**Computational Finance**  
**Mathematical Finance**  
**Portfolio Optimization**  
**Financial Econometrics**  
**Numerical Methods**

---

# 📚 Course

**MA 374 — Financial Engineering**  
**Indian Institute of Technology Guwahati**

This repository contains coursework developed through the computational labs of the course. The implementations and analyses were carried out independently as part of the coursework.

---

> **From mathematical models → numerical algorithms → simulation → market data.**
