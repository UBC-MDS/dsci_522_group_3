# translated my R Code to Python using ChatGPT.
# R Code source: 
# https://github.com/ttimbers/demo-tests-ds-analysis-r/blob/main/R/count_classes.R

import pandas as pd
from sklearn.model_selection import train_test_split

def train_test_split_class(prepared_data_frame, target_col, test_data_ratio, random_state = None, shuffle = True):
    """
    Performs data splitting in terms of training features, training labels, 
    test features, and test labels.

    Parameters:
    ----------
    prepared_data_frame : pandas.DataFrame
        The input DataFrame containing the data to analyze. Note that the
        data frame here is after steps including cleaning and transformation
        that are necessary for upcoming data analysis
    target_col : str
        The name of the column in the DataFrame containing class labels.
    test_data_ratio: float
        The proportion of test data out of the whole dataset
    random_state: integer
        The random seed for data split
    shuffle: boolean
        Whether to shuffle data before splitting the data

    Returns:
    -------
    pandas.DataFrame
        4 DataFrames: X_train, y_train, X_test, y_test:
        - X_train and y_train, X_test and y_test share the same row number.
        - X_test and X_train share the same column number.
        - y_train and y_test both have only one column, with name equal to the
          parameter `target_col`
        
    Examples:
    --------
    >>> import pandas as pd
    >>> from sklearn.model_selection import train_test_split
    >>> data = pd.read_csv('mtcars.csv')  # Replace 'mtcars.csv' with your dataset file
    >>> X_train, y_train, X_test, y_test = train_test_split_class(data, 'target', 0.2, 123, False)
    
    Notes:
    -----
    This function uses the pandas library and train_test_split from sklearn to perform 
    data splitting in terms of training features, training labels, test features, and 
    test labels.

    """

    train_df, test_df = train_test_split(prepared_data_frame, test_size=test_data_ratio, random_state = random_state, shuffle = shuffle)
    features = [col for col in train_df.columns if col != target_col]

    X_train = train_df[features]
    y_train = train_df[target_col]

    X_test = test_df[features]
    y_test = test_df[target_col]

    return X_train, y_train, X_test, y_test