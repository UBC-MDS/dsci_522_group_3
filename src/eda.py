



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
    fig=plt.figure()
    for feat in features:
        train_df.groupby(col)[feat].plot.hist(bins=50, alpha=0.5, legend=True, density=True, title="Histogram of " + feat)
        plt.xlabel(feat)
        
    return fig





# def plot_histograms(train_df, col, features):
#     """
#     Plot histograms for specified features based on the grouping variable.

#     Parameters:
#     - train_df (pd.DataFrame): The DataFrame containing the data.
#     - col (str): The name of the grouping variable.
#     - features (list): List of feature names to plot.

#     Returns:
#     - fig (matplotlib.figure.Figure): The matplotlib Figure object.
#     """
#     fig, axes = plt.subplots(nrows=len(features), ncols=1, figsize=(8, 6*len(features)))

#     for i, feat in enumerate(features):
#         for group_name, group_data in train_df.groupby(col):
#             group_data[feat].plot.hist(bins=50, alpha=0.5, ax=axes[i], legend=True, density=True, title=f"Histogram of {feat} - Grouped by {col}")
        
#         axes[i].set_xlabel(feat)
#         axes[i].legend(title=col)

#     plt.tight_layout()

#     return fig





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
    fig=plt.figure()
    plt.figure(figsize=(8, 8))
    plt.scatter(train_df[x_feature], train_df[y_feature], s=20, c=color, alpha=0.7)
    plt.title(f'Scatter Plot of {x_feature} vs {y_feature}')
    plt.xlabel(f'{x_feature} (%)')
    plt.ylabel(f'{y_feature} (%)')
    

    return fig



