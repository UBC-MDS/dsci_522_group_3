#!/bin/sh

python src/data_read.py \
  --price_name='^gspc' \
  --cpi_link='https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=CPIAUCNS&scale=left&cosd=1913-01-01&coed=2023-09-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-11-11&revision_date=2023-11-11&nd=1913-01-01' \
  --interest_link='https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=DFF&scale=left&cosd=1954-07-01&coed=2023-11-08&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Daily%2C%207-Day&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-11-11&revision_date=2023-11-11&nd=1954-07-01' \
  --gspc_out_path='data/raw/gspc_raw.csv' \
  --cpi_out_path='data/raw/cpi_raw.csv' \
  --interest_out_path='data/raw/interest_raw.csv'

python src/data_clean.py \
  --gspc_raw_path='data/raw/gspc_raw.csv' \
  --cpi_raw_path='data/raw/cpi_raw.csv' \
  --interest_raw_path='data/raw/interest_raw.csv' \
  --out_path='data/processed/cleaned_data.csv'

python src/feature_extract.py \
  --data_path='data/processed/cleaned_data.csv' \
  --out_path='data/processed/processed_data.csv'

python src/train_test_split_class.py \
  --processed_data_path='data/processed/processed_data.csv' \
  --random_state='123' \
  --test_data_ratio='0.2'\
  --x_train_path='data/processed/x_train.csv' \
  --y_train_path='data/processed/y_train.csv' \
  --x_test_path='data/processed/x_test.csv' \
  --y_test_path='data/processed/y_test.csv'

python src/train_test_split_class.py \
  --x_train_path='data/processed/x_train.csv' \
  --y_train_path='data/processed/y_train.csv' \
  --x_test_path='data/processed/x_test.csv' \
  --y_test_path='data/processed/y_test.csv' \
  --out_path='result/tables/mdl_result.csv'
