# Interest Rate Models

This folder contains implementations and analysis of short-rate models for interest-rate dynamics and yield-curve modelling, developed as part of **MA 374 — Financial Engineering**.

## Topics Covered

- Short-rate modelling
- Vasicek model
- CIR (Cox–Ingersoll–Ross) model
- Yield curves
- Term structure of interest rates
- Yield versus time
- Yield versus maturity
- Sensitivity to initial short rates
- Comparison of different model parameter sets

## Lab

### Lab 12 — Vasicek & CIR Models

Implemented and analyzed the Vasicek and CIR short-rate models for different parameter configurations.

The analysis includes:

- Computing and plotting the term structure under the Vasicek model
- Studying yield curves for different initial interest-rate values
- Extending the maturity horizon and examining long-term yield behaviour
- Implementing the CIR model with its square-root diffusion term
- Computing and plotting CIR term structures for different parameter sets
- Studying the effect of varying the initial short rate on yield curves
- Recording observations from the resulting yield-curve behaviour

## Models

### Vasicek Model

The short rate follows:

\[
dr = \beta(\mu-r)\,dt + \sigma\,dW^Q
\]

The model is analyzed for multiple parameter sets and initial short-rate values.

### CIR Model

The short rate follows:

\[
dr = \beta(\mu-r)\,dt + \sigma\sqrt{r}\,dW^Q
\]

The analysis examines the resulting term structures and yield curves across different parameter configurations.

## Key Concepts

**Short-Rate Dynamics → Vasicek Model → CIR Model → Term Structure → Yield Curves → Maturity Analysis**
