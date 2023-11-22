FROM quay.io/jupyter/minimal-notebook:2023-11-19

RUN conda install -y pandas \
  numpy=1.26.0 \
  altair=5.1.2 \
  matplotlib=3.8.2 \
  scikit-learn=1.3.2

RUN mkdir notebook

EXPOSE 8888

RUN pip install yfinance