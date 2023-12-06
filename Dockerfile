FROM quay.io/jupyter/minimal-notebook:2023-11-19

RUN conda install -y -c conda-forge pandas=2.1.3 \
 numpy=1.26.0 \
 altair=5.1.2 \
 matplotlib=3.8.2 \
 scikit-learn=1.3.2

RUN conda install -y -c conda-forge jupyter-book=0.15.1

RUN conda install -y -c anaconda pytest=7.4.0 \
  click=8.1.7

RUN pip install vegafusion-python-embed==1.4.5 \
                vl-convert-python==1.1.0 \
                vegafusion==1.4.5 \
                yfinance==0.2.32

RUN conda install -y -c anaconda make
RUN python -m ipykernel install --user --name conda-env-522Group3-py
