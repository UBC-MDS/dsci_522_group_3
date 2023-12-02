import sys
import os
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.data_read
import src.data_clean
import src.feature_extract


def get_all_data():
    src.data_read.main_inner(price_name='^gspc',
                             cpi_link='https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=CPIAUCNS&scale=left&cosd=1913-01-01&coed=2023-09-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-11-11&revision_date=2023-11-11&nd=1913-01-01',
                             interest_link='https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=DFF&scale=left&cosd=1954-07-01&coed=2023-11-08&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Daily%2C%207-Day&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-11-11&revision_date=2023-11-11&nd=1954-07-01',
                             gspc_out_path='gspc_raw.csv',
                             cpi_out_path='cpi_raw.csv',
                             interest_out_path='interest_raw.csv')

    src.data_clean.main_inner(gspc_raw_path='gspc_raw.csv',
                              cpi_raw_path='cpi_raw.csv',
                              interest_raw_path='interest_raw.csv',
                              out_path='cleaned_data.csv')

    src.feature_extract.main_inner('cleaned_data.csv',
                                   'processed_data.csv')

    df = pd.read_csv('processed_data.csv', index_col=0, parse_dates=True)

    # remove all created csv files
    for f in os.listdir():
        if f.endswith('.csv'):
            os.remove(f)

    return df

def test_read_data():

    all_dat = get_all_data()

    # check is a dataframe
    assert isinstance(all_dat, pd.DataFrame)

    # check column names
    assert list(all_dat.columns) == ['gspc',
                                     'gspc_next_year_pct_chg',
                                     'gspc_prev_year_pct_chg',
                                     'inflation_rate_pct',
                                     'inflation_rate_pct_chg',
                                     'interest_rate_pct',
                                     'interest_rate_pct_chg',
                                     'target']

    # check numeric columns
    assert list(all_dat.select_dtypes(include='float64').columns) == ['gspc',
                                                                      'gspc_next_year_pct_chg',
                                                                      'gspc_prev_year_pct_chg',
                                                                      'inflation_rate_pct',
                                                                      'inflation_rate_pct_chg',
                                                                      'interest_rate_pct',
                                                                      'interest_rate_pct_chg']
    # check boolean columns
    assert list(all_dat.select_dtypes(include='bool').columns) == ['target']

    # check index start and end
    assert all_dat.index[0] == pd.DatetimeIndex(['1955-07-31'])[0]
    assert all_dat.index[-1] == pd.DatetimeIndex(['2022-10-31'])[0]

    # check index is increasing
    assert all_dat.index.is_monotonic_increasing

    # check index is unique
    assert all_dat.index.is_unique

    # check no na
    assert not all_dat.isna().any(axis=None)

    return



def test_median_data():

    test_data = {
        'date': pd.date_range(start='2023-05-01', end='2023-05-31', freq='D'),
        'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    }
    #test_data
    df = pd.DataFrame(test_data)
    df.set_index('date', inplace=True)

    resampled_data = src.data_clean.resample_m_median(df)
    # Check if the returned object is a pandas DataFrame or Series
    assert isinstance(resampled_data, (pd.DataFrame, pd.Series))

    # Check if the resampled data has the correct number of rows (assuming a monthly frequency)
    expected_rows = 1
    assert len(resampled_data) == expected_rows

    # Check if the resampled data has the correct median values
    expected_medians = 16
    assert resampled_data['value'].tolist()[0] == expected_medians

