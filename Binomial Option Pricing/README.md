# Binomial Option Pricing

This folder contains implementations of binomial-tree methods for pricing derivative securities, developed as part of **MA 374 — Financial Engineering**.

The work progresses from basic European option pricing to path-dependent lookback options and American options with early-exercise features.

## Topics Covered

- European call and put option pricing
- Binomial tree construction and backward induction
- Convergence of option prices with increasing number of time steps
- Lookback option pricing
- American call and put option pricing
- Optimal exercise strategy for American options
- Computational comparison of basic and Markov-based binomial algorithms
- Sensitivity of option prices to model parameters

## Labs

### Lab 01 — European Options & Binomial Convergence

Implemented the basic binomial pricing algorithm for European call and put options.

The analysis includes:

- Pricing European call and put options
- Checking the model's no-arbitrage condition
- Studying option prices for different numbers of binomial time steps
- Examining convergence of option prices as the number of steps increases
- Computing option values at different points in time

The model uses continuous compounding and the specified up/down factors from the assignment.

### Lab 02 — Lookback Options & Efficient Binomial Algorithm

Extended the binomial framework to price a European lookback option using the basic binomial algorithm.

The implementation includes:

- Lookback option pricing for different numbers of time steps
- Comparison of option values for different tree sizes
- Computation of option values at intermediate time points
- Implementation of a Markov-based computationally efficient binomial algorithm
- Comparison of the computational performance and scalability of the two approaches

### Lab 03 — American Options & Optimal Exercise

Extended the binomial model to American options, incorporating the possibility of early exercise.

The analysis includes:

- Pricing American call and put options
- Studying the effect of varying model parameters on option prices
- Comparing option prices across different initial stock prices, strike prices, interest rates, volatilities, and numbers of time steps
- Computing American put option values at all time points
- Determining the optimal exercise strategy

## Key Concepts

**Binomial Tree → Backward Induction → Convergence → Path Dependence → Early Exercise → Computational Efficiency**
