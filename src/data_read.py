import pandas as pd
import yfinance as yf


def get_all_data():
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

    comb_all = pd.concat([gspc_data, cpi_data, interest_rate_data],
                         axis=1,
                         join='inner')

    comb_all.dropna(axis=0, inplace=True)
    comb_all['target'] = comb_all['gspc_next_year_pct_chg'] > 0
    comb_all.index.name = 'date'

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

    # re sample to monthly
    gspc_m_s: pd.Series = gspc_raw_s.resample('M').last()
    assert ((gspc_m_s.index
             == pd.date_range(start=gspc_m_s.index[0],
                              end=gspc_m_s.index[-1],
                              freq='M')).all())

    # next year change
    gspc_next_year_pct_chg: pd.Series = (gspc_m_s.shift(-12) - gspc_m_s) / gspc_m_s * 100
    gspc_next_year_pct_chg.name = 'gspc_next_year_pct_chg'


    # previous year change
    gspc_prev_year_pct_chg: pd.Series = (gspc_m_s - gspc_m_s.shift(12)) / gspc_m_s.shift(12) * 100
    gspc_prev_year_pct_chg.name = 'gspc_prev_year_pct_chg'

    # combine all and return
    comb_all = pd.concat([gspc_m_s,
                          gspc_next_year_pct_chg,
                          gspc_prev_year_pct_chg],
                         axis=1,
                         join='inner')

    return comb_all


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

    # offset date by 1 day to get last day of month (original data is first day of month)
    cpi_m_s: pd.Series = cpi_raw_s.copy()
    cpi_m_s.index = cpi_m_s.index - pd.Timedelta(days=1)
    # calculate inflation from cpi
    inflation_rate_m_s: pd.Series = (cpi_m_s - cpi_m_s.shift(12)) / cpi_m_s.shift(12) * 100
    inflation_rate_m_s.name = 'inflation_rate_pct'
    # calculate change in inflation rate
    inflation_rate_chg_m_s: pd.Series = (inflation_rate_m_s
                                         - inflation_rate_m_s.shift(12))
    inflation_rate_chg_m_s.name = 'inflation_rate_pct_chg'

    # combine inflation rate and change in inflation rate and return
    comb_all = pd.concat([inflation_rate_m_s, inflation_rate_chg_m_s],
                         axis=1,
                         join='inner')

    return comb_all


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
    # resample to last day of month and get monthly median
    interest_rate_m_s: pd.Series = resample_m_median(interest_rate_raw_s)
    # calculate change in inflation
    interest_rate_chg_m_s: pd.Series = interest_rate_m_s - interest_rate_m_s.shift(12)
    interest_rate_chg_m_s.name = 'interest_rate_pct_chg'
    # combine inflation and change in inflation in inflation and return
    comb_all = pd.concat([interest_rate_m_s, interest_rate_chg_m_s], axis=1,
                         join='inner')

    return comb_all

def resample_m_median(raw_data):
    """
    Resamples time-series data at a monthly frequency and computes the median for each month.

    Parameters:
    - raw_data: The input time-series data to be resampled.

    Returns:
    - Resampled data with median values for each month.

    Example:
    >>> import pandas as pd
    >>> # Assuming 'raw_data' is a pandas DataFrame or Series with a datetime index
    >>> resampled_data = resample_m_median(raw_data)
    """
    return raw_data.resample('M').median()

