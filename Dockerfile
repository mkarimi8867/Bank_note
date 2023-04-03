FROM continuumio/anaconda3

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ADD . /app

RUN pip install -r requirements
ENV PORT 8080
CMD ["gunicorn","app:main","--config=config.py"]
