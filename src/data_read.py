import pandas as pd
import yfinance as yf


def get_all_data():

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
    assert not gspc_m_s.isna().any()


    # next year change
    gspc_next_year_pct_chg: pd.Series = (gspc_m_s.shift(-12) - gspc_m_s) / gspc_m_s * 100
    gspc_next_year_pct_chg.name = 'gspc_next_year_pct_chg'


    # previous year change
    gspc_prev_year_pct_chg: pd.Series = (gspc_m_s - gspc_m_s.shift(12)) / gspc_m_s.shift(12) * 100
    gspc_prev_year_pct_chg.name = 'gspc_prev_year_pct_chg'

    comb_all = pd.concat([gspc_m_s,
                          gspc_next_year_pct_chg,
                          gspc_prev_year_pct_chg],
                         axis=1,
                         join='inner')

    return comb_all


def read_from_fred(data_link: str, series_name: str):
    raw_s: pd.Series = (pd.read_csv(data_link,
                                    parse_dates=['DATE'])
                        .set_index('DATE')
                        .squeeze())
    raw_s.index.name = 'date'
    raw_s.name = series_name

    return raw_s


def get_cpi_data():
    cpi_raw_s: pd.Series = read_from_fred('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=CPIAUCNS&scale=left&cosd=1913-01-01&coed=2023-09-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-11-11&revision_date=2023-11-11&nd=1913-01-01',
                                          'cpi')

    cpi_m_s: pd.Series = cpi_raw_s.copy()
    cpi_m_s.index = cpi_m_s.index - pd.Timedelta(days=1)
    inflation_rate_m_s: pd.Series = (cpi_m_s - cpi_m_s.shift(12)) / cpi_m_s.shift(12) * 100
    inflation_rate_m_s.name = 'inflation_rate_pct'
    inflation_rate_chg_m_s: pd.Series = (inflation_rate_m_s
                                         - inflation_rate_m_s.shift(12))
    inflation_rate_chg_m_s.name = 'inflation_rate_pct_chg'

    comb_all = pd.concat([inflation_rate_m_s, inflation_rate_chg_m_s],
                         axis=1,
                         join='inner')

    return comb_all


def get_interest_rate_data():

    interest_rate_raw_s = read_from_fred('https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=DFF&scale=left&cosd=1954-07-01&coed=2023-11-08&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Daily%2C%207-Day&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-11-11&revision_date=2023-11-11&nd=1954-07-01',
                   'interest_rate_pct')
    interest_rate_m_s: pd.Series = interest_rate_raw_s.resample('M').median()
    interest_rate_chg_m_s: pd.Series = interest_rate_m_s - interest_rate_m_s.shift(12)
    interest_rate_chg_m_s.name = 'interest_rate_pct_chg'
    comb_all = pd.concat([interest_rate_m_s, interest_rate_chg_m_s], axis=1,
                         join='inner')

    return comb_all
