



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_histograms(train_df, col, features):
    """
    Plot histograms for specified features based on the target variable.

    Parameters:
    - train_df (pd.DataFrame): The DataFrame containing the data.
    - target (str): The name of the target variable.
    - features (list): List of feature names to plot.

    Returns:
    None
    """
    for feat in features:
        train_df.groupby(col)[feat].plot.hist(bins=50, alpha=0.5, legend=True, density=True, title="Histogram of " + feat)
        plt.xlabel(feat)
        plt.show()

# # Test Example:
# # Assuming 'target' is the name of your target variable
# # Create a dummy DataFrame for testing
# data = {'target': np.random.choice([0, 1], size=100),
#         'inflation_rate_pct': np.random.randn(100),
#         'interest_rate_pct': np.random.randn(100),
#         'inflation_rate_pct_chg': np.random.randn(100),
#         'interest_rate_pct_chg': np.random.randn(100),
#         'gspc_prev_year_pct_chg': np.random.randn(100)}

# test_df = pd.DataFrame(data)

# # Call the function with the test DataFrame
# plot_histograms(test_df, 'target', features)

# # Example of using assert for testing
# assert isinstance(test_df, pd.DataFrame), "Input should be a DataFrame"
# print("Test passed!")






def scatter_plot(train_df, x_feature, y_feature, color='blue'):
    """
    Generate a scatter plot for two features in a DataFrame.

    Parameters:
    - train_df (pd.DataFrame): The DataFrame containing the data.
    - x_feature (str): The name of the feature for the x-axis.
    - y_feature (str): The name of the feature for the y-axis.
    - color (str, optional): The color of the scatter plot. Default is 'blue'.

    Returns:
    None
    """
    plt.figure(figsize=(8, 8))
    plt.scatter(train_df[x_feature], train_df[y_feature], s=20, c=color, alpha=0.7)
    plt.title(f'Scatter Plot of {x_feature} vs {y_feature}')
    plt.xlabel(f'{x_feature} (%)')
    plt.ylabel(f'{y_feature} (%)')
    plt.show()

# # Assert test for the function
# # Assuming 'train_df' is the name of your DataFrame
# assert isinstance(train_df, pd.DataFrame), "Input should be a DataFrame"

# # Example usage:
# scatter_plot(train_df, 'interest_rate_pct', 'inflation_rate_pct', color='blue')
# scatter_plot(train_df, 'interest_rate_pct_chg', 'inflation_rate_pct_chg', color='green')
# scatter_plot(train_df, 'inflation_rate_pct_chg', 'inflation_rate_pct', color='red')
# scatter_plot(train_df, 'interest_rate_pct_chg', 'interest_rate_pct', color='blue')



