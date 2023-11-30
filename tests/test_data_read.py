import sys
import os
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import src.data_read
import src.data_clean
import src.fea_extract


def get_all_data():
    src.data_read.main('data/gspc_raw_tmp',
                       'data/cpi_raw_tmp',
                       'data/interest_raw_tmp')

    src.data_clean.main('data/gspc_raw_tmp',
                        'data/cpi_raw_tmp',
                        'data/interest_raw_tmp',
                        'data/clean_tmp')

    src.data_extract.main('data/clean_tmp',
                          'data/final_tmp')

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
    assert all_dat.index[0] == pd.DatetimeIndex(['1955-07-31'])
    assert all_dat.index[-1] == pd.DatetimeIndex(['2022-10-31'])

    # check index is increasing
    assert all_dat.index.is_monotonic_increasing

    # check index is unique
    assert all_dat.index.is_unique

    # check no na
    assert not all_dat.isna().any(axis=None)

    return


#sample data for testing median

# df


def test_median_data():

    test_data = {
        'date': pd.date_range(start='2023-05-01', end='2023-05-31', freq='D'),
        'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    }
    #test_data
    df = pd.DataFrame(test_data)
    df.set_index('date', inplace=True)

    resampled_data = src.data_read.resample_m_median(df)
    # Check if the returned object is a pandas DataFrame or Series
    assert isinstance(resampled_data, (pd.DataFrame, pd.Series))

    # Check if the resampled data has the correct number of rows (assuming a monthly frequency)
    expected_rows = 1
    assert len(resampled_data) == expected_rows

    # Check if the resampled data has the correct median values
    expected_medians = 16 
    assert resampled_data['value'].tolist()[0] == expected_medians

#test_median_data()