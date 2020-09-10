FROM python:3.8

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY *.py /app/
COPY database/*.py /app/database/
CMD python main.py