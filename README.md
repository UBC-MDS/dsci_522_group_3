---
editor_options: 
  markdown: 
    wrap: 72
---

# Predicting Direction of Stock Price from Interest Rate and Inflation Rate

-   Authors: Allen Lee, Jianhao Zhang, Chengyu Tao, Yi Yan

A demo of a data analysis project for DSCI 522 (Data Science workflows);
a course in the Master of Data Science program at the University of
British Columbia.

[![Photo by Alexander Schimmeck on
Unsplash](images/alexander-schimmeck-WhBMPxr2RhA-unsplash (1).jpg)](https://unsplash.com/photos/10-10-and-10-us-dollar-bill-WhBMPxr2RhA)

## About

During the COVID-19 pandemic, central banks around the world lowered
interest rates to ease economical challenges posed by the pandemic. As
the pandemic ease, the lowered interest rate leads to excess consumer
spending which increased the inflation rate to unacceptable levels. In
order to control the inflation and have it return to pre-pandemic
levels, the central bank raised the interest rate sharply to the highest
level in 15 years. Nowadays, inflation and interest rate often takes the
headline of financial news and with more than 50% of American households
owning stocks, our team is curious to find out how inflation and
interest rate affect stock returns. We ask the question: given inflation
rate and interest rate data, can we predict whether we will profit if we
invest in a stock market index and hold for 1 year.

## Data and Method

This project uses Standard & Poors 500 Index (S&P500) as stock market
proxy. The index tracks stocks of 500 largest companies in USA. The
price of S&P500 is obtained from Yahoo Finance.

Inflation data is obtained from calculating the change of consumer price
index (CPI). The United States CPI is obtained from the Federal Reserve
Economic Data website and then computed yearly inflation rate.

## Report

The final report can be found
[here](https://ubc-mds.github.io/dsci_522_group_3/src/predicting_direction_of_stock_price_from_inflation_rate_and_interest_rate.html).

## Usage

Run the following code in terminal when first opening the project:

``` bash
conda env create --file environment.yaml
```

To run the analysis, run the following from the root of repository:

``` bash
conda activate 522Group3
```

To jupyter lab from the root of repository:

``` bash
jupyter lab 
```

Open
`src/predicting_direction_of_stock_price_from_inflation_rate_and_interest_rate.ipynb`
in Jupyter Lab and click "Restart Kernel and Run All Cell".

## Dependencies

-   `conda` (version 23.9.0 or higher)
-   `nb_conda_kernels` (version 2.3.1 or higher)
-   Python and other packages listed in `environment.yaml`

## License

Copyright (c) 2023 Master of Data Science at the University of British
Columbia. Detailed information please refer to LICENSE.md.

## References

::: {#refs .references .hanging-indent}
<div>

Yahoo!. S&P 500 (\^GSPC) charts, Data & News. Yahoo! Finance.
<https://ca.finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC&.tsrc=fin-srch>

</div>
:::
