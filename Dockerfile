FROM continuumio/anaconda3

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH

COPY . /app
EXPOSE 5000
WORKDIR /app
RUN pip install -r requirements
CMD python main.py
