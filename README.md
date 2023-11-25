# Predicting Direction of Stock Price from Interest Rate and Inflation Rate

-   Authors: Allen Lee, Jianhao Zhang, Chengyu Tao, Yi Yan

A demo of a data analysis project for DSCI 522 (Data Science workflows); a course in the Master of Data Science program at the University of British Columbia.

![Photo by Alexander Schimmeck on Unsplash](images/img.jpg)

## About

During the COVID-19 pandemic, central banks around the world lowered interest rates to ease economical challenges posed by the pandemic. As the pandemic ease, the lowered interest rate leads to excess consumer spending which increased the inflation rate to unacceptable levels. In order to control the inflation and have it return to pre-pandemic levels, the central bank raised the interest rate sharply to the highest level in 15 years. Nowadays, inflation and interest rate often takes the headline of financial news and with more than 50% of American households owning stocks, our team is curious to find out how inflation and interest rate affect stock returns. We ask the question: given inflation rate and interest rate data, can we predict whether we will profit if we invest in a stock market index and hold for 1 year.

## Report

The final report can be found [here](https://ubc-mds.github.io/stock_price_direction_prediction_from_interest_and_inflation_rate/src/predicting_direction_of_stock_price_from_inflation_rate_and_interest_rate.html).

## Dependencies

Docker is a container solution used to manage the software dependencies for this project. The Docker image used for this project is based on the 
```
quay.io/jupyter/minimal-notebook:2023-11-19 image.
```
More detailed dependencies are specified in the [Dockerfile](https://github.com/UBC-MDS/stock_price_direction_prediction_from_interest_and_inflation_rate/blob/main/Dockerfile). 

## Usage

### Setup

1. Install and launch Docker on your computer from the website: https://www.docker.com/get-started/

2. Clone the GitHub repository.

### Running the analysis
1. Open the Docker app.
  
2. Enter the following command in the terminal.
```         
docker compose up
```

3. In the terminal, look for a URL that starts with http://127.0.0.1:8888/lab?token=. Copy and paste that URL into your browser.

![Photo of terminal](images/container.jpg)

4. Open src/predicting_direction_of_stock_price_from_inflation_rate_and_interest_rate.ipynb in Jupyter Lab and click "Restart Kernel and Run All Cell".

### Clean up
1. To shut down the container and clean up the resources, type Cntrl + C in the terminal where you launched the container, and then type 'docker compose rm'

## Developer notes

#### Adding a new dependency (cite from Tiffany's [repo](https://github.com/ttimbers/breast_cancer_predictor_py/tree/v1.0.0) )

1.  Add the dependency to the `Dockerfile` file on a new branch.

2.  Re-build the Docker image locally to ensure it builds and runs
    properly.

3.  Push the changes to GitHub. A new Docker image will be built and
    pushed to Docker Hub automatically.

4.  Update the `docker-compose.yml` file on your branch to use the new
    container image.

5.  Send a pull request to merge the changes into the `main` branch.

#### Running the tests

Tests are run using the `pytest` command in the root of the project.
More details about the test suite can be found in the `tests` directory.
```
pytest tests/*
```
## License

Copyright (c) 2023 Master of Data Science at the University of British Columbia. Detailed information please refer to LICENSE.md.

## References

Yahoo!. S&P 500 (\^GSPC) charts, Data & News. Yahoo! Finance. <https://ca.finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC&.tsrc=fin-srch>
