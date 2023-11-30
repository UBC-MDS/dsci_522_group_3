import pandas as pd
import yfinance as yf


def main(gspc_out_path, cpi_out_path, interest_out_path):
    """
    Combine three datasets to create a consolidated DataFrame.
    Retrieve data on the S&P 500 index (gspc_data),
    Consumer Price Index (cpi_data), and interest rates (interest_rate_data).

    Returns:
    - DataFrame: A consolidated DataFrame containing financial and economic data.
    
    Example:
    >>> combined_data = get_all_data()
    >>> print(combined_data.head())
    """
    # call all function to get all data then combine and return.

    gspc_data = get_gspc_data()
    cpi_data = get_cpi_data()
    interest_rate_data = get_interest_rate_data()


    gspc_data.to_csv(gspc_out_path)
    cpi_data.to_csv(cpi_out_path)
    interest_rate_data.to_csv(interest_out_path)

    return comb_all


def get_gspc_data():
    """
    Retrieves historical data for the S&P 500 index (^GSPC) from Yahoo Finance, 
    performs data preprocessing, and calculates percentage changes over the next and previous years.

    Resample data into a monthly frequency, and calculate next year and previous year change.

    Returns:
    - Dataframe: A DataFrame containing S&P 500 data.

    Example:
    >>> cpi_data = get_cpi_data()
    >>> print(cpi_data.head())
    """

    # read raw
    gspc_raw_s: pd.Series = (yf
                             .Ticker('^GSPC')
                             .history(start='1950-01-01',
                                      end='2023-11-01')
                             .loc[:, 'Close'])
    gspc_raw_s.name = 'gspc'
    gspc_raw_s.index = pd.DatetimeIndex(gspc_raw_s.index.date)
    gspc_raw_s.index.name = 'date'

    return gspc_raw_s


def read_from_fred(data_link: str, series_name: str):
    """
    Reads time-series data from the Federal Reserve Economic Data (FRED) using a provided data link.

    Parameters:
    - data_link (str): The URL/local file path of the CSV file.
    - series_name (str): The name to assign to the outputting Series.

    Returns:
    - Series: A series representing the specified economic series.

    """
    # reads data from federal reserve

    raw_s: pd.Series = (pd.read_csv(data_link,
                                    parse_dates=['DATE'])
                        .set_index('DATE')
                        .squeeze())
    raw_s.index.name = 'date'
    raw_s.name = series_name

    return raw_s


def get_cpi_data():
    """
    Retrieves and processes Consumer Price Index (CPI) data from the Federal Reserve Economic Data (FRED).
    
    Returns:
    - DataFrame: A DataFrame containing CPI-related data, including the monthly inflation rate
                 and the change in inflation rate over the previous year.

    Example:
    >>> cpi_data = get_cpi_data()
    >>> print(cpi_data.head())
    """
    # reads raw cpi data
    cpi_raw_s: pd.Series = read_from_fred('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=CPIAUCNS&scale=left&cosd=1913-01-01&coed=2023-09-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-11-11&revision_date=2023-11-11&nd=1913-01-01',
                                          'cpi')

    return cpi_raw_s


def get_interest_rate_data():
    """
    Retrieves and processes interest rate data from the Federal Reserve Economic Data (FRED).

    Return:
    - DataFrame

    Example:
    >>> interest_rate_data = get_interest_rate_data()
    >>> print(interest_rate_data.head())
    """

    # read raw interest rate data
    interest_rate_raw_s = read_from_fred('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=DFF&scale=left&cosd=1954-07-01&coed=2023-11-08&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Daily%2C%207-Day&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-11-11&revision_date=2023-11-11&nd=1954-07-01',
                   'interest_rate_pct')

    return interest_rate_raw_s


if __name__ == '__main__':
    main()

