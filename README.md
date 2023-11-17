---
editor_options: 
  markdown: 
    wrap: 72
---

# Stock Prediction

-   Authors: Allen Lee, Jianhao Zhang, Chengyu Tao, Yi Yan

A demo of a data analysis project for DSCI 522 (Data Science workflows);
a course in the Master of Data Science program at the University of
British Columbia.

## About

brief introduce about our project scope, expected outcome, raw data, and
methods we are going to use.

During the COVID-19 pandemic, central banks around the world lowered
interest rates to ease economical challenges posed by the pandemic. As
the pandemic ease, the lowered interest rate leads to excess consumer
spending which increased the inflation rate to unacceptable levels. In
order to control the inflation and have it return to pre-pandemic
levels, the central bank raised the interest rate sharply to the highest
level in 15 years. Nowadays, inflation and interest rate often takes the
headline of financial news and with more than 50% of American households
own stocks, our team is curious to find out how inflation and interest
rate affect stock returns.

## Data and Method

1\. We can use the Standard & Poors 500 Index (S&P500) as stock market
proxy. The index tracks stocks of 500 largest companies in USA.

2\. To obtain inflation, we simpy calculate the change of consumer price
index (CPI).

3\. We can use the Federal funds rate as proxy for interest rate. It is
the target interest rate set by the Federal reserve for commercial banks
to lend and borrow overnight.

4\. We will use Exploratory data analysis (EDA) to predict the model.

## Report

The final report can be found here. (add report link later)

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

Open `src/stock_value_report.ipynb` in Jupyter Lab and click "Restart
Kernel and Run All Cell".

(probably need to change report name!!!!)

## Dependencies

-   `conda` (version 23.9.0 or higher)
-   `nb_conda_kernels` (version 2.3.1 or higher)
-   Python and packages listed in `environment.yaml`

## License

Copyright (c) 2023 Master of Data Science at the University of British
Columbia. Detailed information please refer to LICENSE.md.

## References

::: {#refs .references .hanging-indent}
::: {#ref-Dua2019}
APA input later
:::

::: {#ref-Streetetal}
:::
:::
