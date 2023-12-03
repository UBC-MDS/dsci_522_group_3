import pandas as pd
import yfinance as yf
import click
import os


@click.command()
@click.option('--price_name', type=str, help='yahoo finance name for price data')
@click.option('--cpi_link', type=str, help='link for cpi data')
@click.option('--interest_link', type=str, help='link for interest data')
@click.option('--gspc_out_path', type=str, help='path to store gspc csv')
@click.option('--cpi_out_path', type=str, help='path to store cpi csv')
@click.option('--interest_out_path', type=str, help='path to store interest csv')
def main(price_name,
         cpi_link,
         interest_link,
         gspc_out_path,
         cpi_out_path,
         interest_out_path):
    """
    read price, CPI and interest rate raw data and store them as
    3 seperate csv files
    this function is for call from terminal
    """
    main_inner(price_name,
               cpi_link,
               interest_link,
               gspc_out_path,
               cpi_out_path,
               interest_out_path)

    return


def main_inner(price_name,
               cpi_link,
               interest_link,
               gspc_out_path,
               cpi_out_path,
               interest_out_path):

    # Check if the folder exists
    if not os.path.exists("data"):
        # If not, create the folder
        os.makedirs("data")

    if not os.path.exists("data/raw"):
        # If not, create the folder
        os.makedirs("data/raw")

    """
    read price, CPI and interest rate raw data and store them as
    3 seperate csv files
    this function is for call from other functions or terminal
    """
    # call all function to get all data then combine and return.
    gspc_data = get_gspc_data(price_name)
    cpi_data = get_cpi_data(cpi_link)
    interest_rate_data = get_interest_rate_data(interest_link)

    gspc_data.to_csv(gspc_out_path)
    cpi_data.to_csv(cpi_out_path)
    interest_rate_data.to_csv(interest_out_path)

    return


def get_gspc_data(price_name_link):
    """
    Retrieves historical data for the S&P 500 index (^GSPC) from Yahoo Finance and return
    it as series
    """

    # read raw
    gspc_raw_s: pd.Series = (yf
                             .Ticker(price_name_link)
                             .history(start='1950-01-01',
                                      end='2023-11-01')
                             .loc[:, 'Close'])
    gspc_raw_s.name = 'gspc'
    gspc_raw_s.index = pd.DatetimeIndex(gspc_raw_s.index.date)
    gspc_raw_s.index.name = 'date'
    gspc_raw_s.sort_index()
    return gspc_raw_s


def read_from_fred(data_link: str, series_name: str):
    """
    Retrieves historical data from federal reserve and store return as series
    """

    raw_s: pd.Series = (pd.read_csv(data_link,
                                    parse_dates=['DATE'])
                        .set_index('DATE')
                        .squeeze())
    raw_s.index.name = 'date'
    raw_s.name = series_name
    raw_s.sort_index()
    return raw_s


def get_cpi_data(cpi_link):
    """
    Retrieves Consumer Price Index (CPI) data from the Federal Reserve Economic Data (FRED).
    and returns as series
    """
    # reads raw cpi data
    cpi_raw_s: pd.Series = read_from_fred(cpi_link, 'cpi')

    return cpi_raw_s


def get_interest_rate_data(interest_link):
    """
    Retrieves interest rate data from the Federal Reserve Economic Data (FRED)
    and return as series
    """

    # read raw interest rate data
    interest_rate_raw_s = read_from_fred(interest_link, 'interest_rate_pct')

    return interest_rate_raw_s


if __name__ == '__main__':
    main()

