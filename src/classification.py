import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import precision_score
import click
import os

@click.command()
@click.option('--x_train_path', type=str)
@click.option('--y_train_path', type=str)
@click.option('--x_test_path', type=str)
@click.option('--y_test_path', type=str)
@click.option('--out_path', type=str)
def main(x_train_path,
         y_train_path,
         x_test_path,
         y_test_path,
         out_path):

    if not os.path.exists('results'):
        os.makedirs('results')
    if not os.path.exists('results/tables'):
        os.makedirs('results/tables')

    X_train = pd.read_csv(x_train_path, index_col=0, parse_dates=True)
    y_train = pd.read_csv(y_train_path, index_col=0, parse_dates=True)
    X_test = pd.read_csv(x_test_path, index_col=0, parse_dates=True)
    y_test = pd.read_csv(y_test_path, index_col=0, parse_dates=True)

    numerical_features = ['inflation_rate_pct', 'interest_rate_pct',
           'inflation_rate_pct_chg', 'interest_rate_pct_chg',
           'gspc_prev_year_pct_chg']

    #Create Column Transformer 
    preprocessor = make_column_transformer(    
        (StandardScaler(), numerical_features),  
    )

    pipe = make_pipeline(preprocessor, LogisticRegression())
    pipe.fit(X_train, y_train)

    y_dummy = pipe.predict(X_test)
    mdl_score = precision_score(y_test, y_dummy)

    dc = DummyClassifier()
    dc.fit(X_train, y_train)
    y_dc = dc.predict(X_test)
    dummy_score = precision_score(y_test, y_dc)


    df = pd.DataFrame(data={'dummy_model_precision_score (%)': [round(dummy_score * 100, 2)], 
                            'logistic_regression_precision_score (%)': [round(mdl_score * 100, 2)]})
    df.to_csv(out_path)
    return


if __name__ == '__main__':
    main()
