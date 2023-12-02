import pandas as pd
import click


def gspc_extract(data):
    """
    extract next year change, previous year change
    and whether next year increased from cleaned data.
    """

    # next year change
    gspc_next_year_pct_chg: pd.Series = (data.shift(-12) - data) / data * 100.0
    gspc_next_year_pct_chg.name = 'gspc_next_year_pct_chg'

    # previous year change
    gspc_prev_year_pct_chg: pd.Series = (data - data.shift(12)) / data.shift(12) * 100
    gspc_prev_year_pct_chg.name = 'gspc_prev_year_pct_chg'

    # target
    tar = gspc_next_year_pct_chg > 0
    tar.name = 'target'

    return pd.concat([gspc_next_year_pct_chg,
                      gspc_prev_year_pct_chg,
                      tar,
                      data], axis=1, join='inner')


def cpi_extract(data):
    """
    extract inflation rate and change in inflation rate from cpi data.
    """

    inflation_rate_m_s: pd.Series = (data - data.shift(12)) / data.shift(12) * 100
    inflation_rate_m_s.name = 'inflation_rate_pct'

    # calculate change in inflation rate
    inflation_rate_chg_m_s: pd.Series = (inflation_rate_m_s
                                         - inflation_rate_m_s.shift(12))
    inflation_rate_chg_m_s.name = 'inflation_rate_pct_chg'

    return pd.concat([inflation_rate_m_s,
                      inflation_rate_chg_m_s], axis=1, join='inner')


def interest_rate_extract(data):
    """
    extract inflation rate and change in inflation rate from cpi data.
    """

    # calculate yearly change in interest rate
    interest_rate_chg_m_s: pd.Series = data - data.shift(12)
    interest_rate_chg_m_s.name = 'interest_rate_pct_chg'

    return pd.concat([interest_rate_chg_m_s, data],
                     axis=1, join='inner')


@click.command()
@click.option('--data_path')
@click.option('--out_path')
def main(data_path, out_path):
    """
    reads cleaned data and extract features for s&p500, cpi and interest rate
    for call from terminal
    """

    main_inner(data_path, out_path)

    return


def main_inner(data_path, out_path):
    """
    reads cleaned data and extract features for s&p500, cpi and interest rate
    for call from test or other functions.
    """

    data = pd.read_csv(data_path, index_col=0, parse_dates=True)

    gspc_f = gspc_extract(data['gspc'].dropna())
    cpi_f = cpi_extract(data['cpi'].dropna())
    interest_f = interest_rate_extract(data['interest_rate_pct'].dropna())

    all_data = pd.concat([gspc_f,
                          cpi_f,
                          interest_f],
                         axis=1, join='inner')

    all_data.sort_index(axis=0, inplace=True)
    all_data.sort_index(axis=1, inplace=True)
    all_data.dropna(axis=0, inplace=True)


    all_data.to_csv(out_path)

    return


if __name__ == '__main__':
    main()
