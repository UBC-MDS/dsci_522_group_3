import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
import click
import os

@click.command()
@click.option()
@click.option('--x_train_path', type=str)
@click.option('--y_train_path', type=str)
@click.option('--x_test_path', type=str)
@click.option('--y_test_path', type=str)
@click.option('--out_path', type=str)
def main(X_train_path,
         y_train_path,
         X_test_path,
         y_test_path,
         out_path)

    if not os.path.exists('results'):
        os.makedirs('results')
    if not os.path.exists('results/tables'):
        os.makedirs('results/tables')

    X_train = pd.read_csv(X_train_path, index_col=0, parse_dates=True)
    y_train = pd.read_csv(y_train_path, index_col=0, parse_dates=True)
    X_test = pd.read_csv(X_test_path, index_col=0, parse_dates=True)
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
    mdl_score = pipe.score(X_test, y_test)

    dc = DummyClassifier()
    dc.fit(X_train, y_train)
    dummy_score = dc.score(X_test, y_test)

    df = pd.Dataframe(data=[dummy_score, mdl_score],
                      index=['dummy_model_score',
                             'logistic_regression_score'])
    df.to_csv(out_path)

    return


if __name__ == '__main__':
    main()
