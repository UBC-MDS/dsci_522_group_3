


import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
import numpy as np


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import src.eda 



def test_plot_histograms():
    # Create a dummy DataFrame for testing
    data = {'target': [0, 1] * 50,
            'inflation_rate_pct': np.random.randn(100),
            'interest_rate_pct': np.random.randn(100),
            'inflation_rate_pct_chg': np.random.randn(100),
            'interest_rate_pct_chg': np.random.randn(100),
            'gspc_prev_year_pct_chg': np.random.randn(100)}

    test_df = pd.DataFrame(data)

    # Call the function with the test DataFrame
    src.eda.plot_histograms(test_df, 'target', list(test_df.columns[1:]))  # Assuming the columns are the features

    # Check is a figure
    result_figure = plt.gcf()

    assert isinstance(result_figure, plt.Figure), f"Expected a matplotlib.figure.Figure, but got {type(obj)}."


    return




def test_scatter_plot():
    # Create a dummy DataFrame for testing
    data = {'target': [0, 1] * 50,
            'inflation_rate_pct': np.random.randn(100),
            'interest_rate_pct': np.random.randn(100),
            'inflation_rate_pct_chg': np.random.randn(100),
            'interest_rate_pct_chg': np.random.randn(100),
            'gspc_prev_year_pct_chg': np.random.randn(100)}

    test_df = pd.DataFrame(data)

    # Call the function with the test DataFrame
    src.eda.scatter_plot(test_df, 'interest_rate_pct', 'inflation_rate_pct', color='blue')

    # Check is a figure
    result_figure = plt.gcf()

    assert isinstance(result_figure, plt.Figure), f"Expected a matplotlib.figure.Figure, but got {type(obj)}."


    return




# # Run the tests
# test_plot_histograms()
# test_scatter_plot()



