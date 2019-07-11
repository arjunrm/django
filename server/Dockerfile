FROM python:3.6

WORKDIR /usr/src/app

# copy project files into the WORKDIR
COPY ./mysite .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD exec gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 --workers 3
