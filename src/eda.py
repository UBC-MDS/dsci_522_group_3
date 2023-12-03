

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import click
import os

import altair as alt





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
    #fig=plt.figure()
    # for feat in features:
    #     train_df.groupby(col)[feat].plot.hist(bins=50, alpha=0.5, legend=True, density=True, title="Histogram of " + feat)
    #     plt.xlabel(feat)
        
    #return fig


    # train_df.groupby(col)[feat].plot.hist(bins=50, alpha=0.5, legend=True, density=True, title="Histogram of " + feat)
    # plt.xlabel(feat,fontsize=10)


    fig, axes = plt.subplots(2,3, figsize=(12, 10))

    for i in range(len(features)):
        plt.subplot(2,3,i+1)
        train_df.groupby(col)[features[i]].plot.hist(bins=50, alpha=0.5, legend=True, density=True, title="Histogram of " + features[i])

    plt.subplot(2, 3, 6).axis('off')

    plt.tight_layout()

    return fig







def scatter_plot(train_df, figsize=(8, 6)):
    """
    Generate a scatter plot for two features in a DataFrame.

    Parameters:
    - train_df (pd.DataFrame): The DataFrame containing the data.
    - x_feature (str): The name of the feature for the x-axis.
    - y_feature (str): The name of the feature for the y-axis.
    - color (str, optional): The color of the scatter plot. Default is 'blue'.
    - figsize (tuple, optional): Figure size. Default is (8, 6).

    Returns:
    - fig (matplotlib.figure.Figure): The Matplotlib figure containing the scatter plot.
    """
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=figsize)

    # Scatter plot for the main axes
    plt.subplot(2, 2, 1)
    plt.scatter(train_df['interest_rate_pct'], train_df['inflation_rate_pct'], s=20, c='blue', alpha=0.7)
    plt.title(f'Scatter Plot of interest_rate_pct vs inflation_rate_pct', fontsize=8)
    plt.xlabel(f'interest_rate_pct (%)', fontsize=8)
    plt.ylabel(f'inflation_rate_pct (%)', fontsize=8)


    # Scatter plot 2
    plt.subplot(2, 2, 2)
    plt.scatter(train_df['interest_rate_pct_chg'], train_df['inflation_rate_pct_chg'], s=20, c='green', alpha=0.7)
    plt.title('Scatter Plot of interest_rate_pct_chg vs inflation_rate_pct_chg', fontsize=8)
    plt.xlabel('interest_rate_pct_chg (%)', fontsize=8)
    plt.ylabel('inflation_rate_pct_chg (%)', fontsize=8)


    plt.subplot(2, 2, 3)
    plt.scatter(train_df['inflation_rate_pct_chg'], train_df['inflation_rate_pct'], s=20, c='red', alpha=0.7)
    plt.title(f'Scatter Plot of interest_rate_pct vs inflation_rate_pct', fontsize=8)
    plt.xlabel(f'inflation_rate_pct_chg (%)', fontsize=8)
    plt.ylabel(f'inflation_rate_pct (%)', fontsize=8)



    # Scatter plot 3
    plt.subplot(2, 2, 4)
    plt.scatter(train_df['interest_rate_pct_chg'], train_df['interest_rate_pct'], s=20, c='blue', alpha=0.7)
    plt.title('Scatter Plot of interest_rate_pct_chg vs interest_rate_pct', fontsize=8)
    plt.xlabel('interest_rate_pct_chg (%)', fontsize=8)
    plt.ylabel('interest_rate_pct (%)', fontsize=8)

    # Adjust layout to prevent clipping
    plt.tight_layout()

    return fig



def create_repeat_line_plots(data_df, repeated_fields, figsize=(20, 18)):
    # Set up the figure and axes
    fig, axes = plt.subplots(8,1, figsize=figsize)

    # Plot each field in a subplot
    for i, field in enumerate(repeated_fields, 1):
        plt.subplot(8,1,i)
        plt.plot(data_df[field])
        plt.title(field, fontsize=12)
        plt.xlabel('Date',fontsize=12)
        plt.ylabel(field,fontsize=12)

    # Adjust layout to prevent clipping
    plt.tight_layout()

    return fig





@click.command()

@click.option('--processed_data_path')
@click.option('--x_train_path')
@click.option('--y_train_path')
@click.option('--time_path')
@click.option('--hist_path')
@click.option('--scat_path')



def main(processed_data_path, x_train_path, y_train_path, time_path, hist_path, scat_path):
    """
    reads cleaned data and extract features for s&p500, cpi and interest rate
    for call from terminal
    """

    main_inner(processed_data_path, x_train_path, y_train_path,time_path, hist_path, scat_path)

    return


def main_inner(processed_data_path, x_train_path, y_train_path, time_path,hist_path, scat_path):
    """
    reads cleaned data and extract features for s&p500, cpi and interest rate
    for call from test or other functions.
    """


    # Check if the folder exists
    if not os.path.exists("results"):
        # If not, create the folder
        os.makedirs("results")

    if not os.path.exists("results/figures"):
        # If not, create the folder
        os.makedirs("results/figures")





    X_train = pd.read_csv(x_train_path, index_col=0, parse_dates=True)
    y_train = pd.read_csv(y_train_path, index_col=0, parse_dates=True)
    processed_data = pd.read_csv(processed_data_path, index_col=0, parse_dates=True)


    data = pd.concat([X_train, y_train], axis=1)




    repeated_fields = ['gspc', 'inflation_rate_pct', 'interest_rate_pct', 'inflation_rate_pct_chg',
                   'interest_rate_pct_chg', 'gspc_prev_year_pct_chg', 'gspc_next_year_pct_chg',
                   'target']

    create_repeat_line_plots(processed_data, repeated_fields).savefig(time_path)





    col="target"
    features = ['inflation_rate_pct', 'interest_rate_pct',
       'inflation_rate_pct_chg', 'interest_rate_pct_chg',
       'gspc_prev_year_pct_chg']


    plot_histograms(data, col, features).savefig(hist_path)


    scatter_plot(data).savefig(scat_path)



    return


if __name__ == '__main__':
    main()
    #main_inner(processed_data_path, x_train_path, y_train_path,time_path, hist_path, scat_path)
