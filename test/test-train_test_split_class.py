import pandas as pd
import pytest
import sys
import os

# Import the train_test_split_class function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.train_test_split_class import train_test_split_class



# Test for correct return type
def test_output_type():
    data = pd.DataFrame({
        'feature1': range(10),
        'feature2': range(10, 20),
        'target': [0, 1] * 5
    })
    target_col = 'target'
    X_train, y_train, X_test, y_test = train_test_split_class(data, target_col, 0.2)
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(y_train, pd.Series)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_test, pd.Series)

# Test split ratio
def test_split_ratio():
    data = pd.DataFrame({
        'feature1': range(100),
        'feature2': range(100, 200),
        'target': [0 if i < 50 else 1 for i in range(100)]
    })
    target_col = 'target'
    test_ratio = 0.2
    X_train, y_train, X_test, y_test = train_test_split_class(data, target_col, test_ratio)
    assert len(X_train) / len(data) == 0.8
    assert len(X_test) / len(data) == 0.2


# test_output_type()
# test_split_ratio()