import pandas as pd


def gspc_extract(data):

    # next year change
	gspc_next_year_pct_chg: pd.Series = (data.shift(-12) - data) / data * 100
    gspc_next_year_pct_chg.name = 'gspc_next_year_pct_chg'

    # previous year change
    gspc_prev_year_pct_chg: pd.Series = (data - data.shift(12)) / data.shift(12) * 100
    gspc_prev_year_pct_chg.name = 'gspc_prev_year_pct_chg'

    return pd.concat([gspc_next_year_pct_chg,
    	              gspc_prev_year_pct_chg], axis=1, join='inner')

def cpi_extract(data):

    inflation_rate_m_s: pd.Series = (data - data.shift(12)) / data.shift(12) * 100
    inflation_rate_m_s.name = 'inflation_rate_pct'

    # calculate change in inflation rate
    inflation_rate_chg_m_s: pd.Series = (inflation_rate_m_s
                                         - inflation_rate_m_s.shift(12))
    inflation_rate_chg_m_s.name = 'inflation_rate_pct_chg'

    return pd.concat([inflation_rate_m_s,
    	              inflation_rate_chg_m_s], axis=1, join='inner')


def interest_rate_extract(data)

    # calculate change in inflation
    interest_rate_chg_m_s: pd.Series = data - data.shift(12)
    interest_rate_chg_m_s.name = 'interest_rate_pct_chg'

    return interest_rate_chg_m_s


def main(data_path
	     out_path)

	data = pd.read_csv(data_path)

	gspc_f = gspc_extract(data['gspc'])
	cpi_f = cpi_extract(data['cpi'])
	interest_f = interest_rate_extract(data['interest_rate_pct'])

	all_data = pd.concat([gspc_f,
		                  cpi_f,
		                  interest_f],
		                  axis=1, join='inner')

	all_data.to_csv(out_path)

	return
