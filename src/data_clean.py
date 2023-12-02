import pandas as pd
import click


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


def clean_gspc_data(gspc_raw):
    """
    resamples S&P500 data to last date of month
    """
    return gspc_raw.resample('M').last()


def clean_cpi_data(cpi_raw):
    """
    cpi raw data is monthly on first date of month.
    this function subtracts all dates by 1 to become last day of last month
    to align with other data.
    """
    cpi_m_s: pd.Series = cpi_raw.copy()
    cpi_m_s.index = cpi_m_s.index - pd.Timedelta(days=1)

    return cpi_m_s


def clean_interest_rate_data(interest_rate_raw):
    """
    resamples to monthly median
    """
    return resample_m_median(interest_rate_raw)


@click.command()
@click.option('--gspc_raw_path', type=str)
@click.option('--cpi_raw_path', type=str)
@click.option('--interest_raw_path', type=str)
@click.option('--out_path', type=str)
def main(gspc_raw_path,
         cpi_raw_path,
         interest_raw_path,
         out_path):

    """
    reads saved raw data, for s&p500, CPI, and interest rate
    resamples s&p500, CPI to last day of month.
    resamples interest rate data with monthly media to last day of month
    this function is for call from terminal
    """

    main_inner(gspc_raw_path,
               cpi_raw_path,
               interest_raw_path,
               out_path)

    return


def main_inner(gspc_raw_path,
               cpi_raw_path,
               interest_raw_path,
               out_path):
    """
    reads saved raw data, for s&p500, CPI, and interest rate
    resamples s&p500, CPI to last day of month.
    resamples interest rate data with monthly media to last day of month
    this function is for call tests or other functions
    """

    gspc = pd.read_csv(gspc_raw_path, index_col=0, parse_dates=True).squeeze()
    cpi = pd.read_csv(cpi_raw_path, index_col=0, parse_dates=True).squeeze()
    interest = pd.read_csv(interest_raw_path, index_col=0, parse_dates=True).squeeze()

    gspc_c = clean_gspc_data(gspc)
    cpi_c = clean_cpi_data(cpi)
    interest_c = clean_interest_rate_data(interest)

    all_dat = pd.concat([gspc_c, cpi_c, interest_c], axis=1, join='outer')
    all_dat.to_csv(out_path)

    return


if __name__ == '__main__':

    main()
