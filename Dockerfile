FROM python:3.9.18-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

# RUN apt update && apt install -y libxslt-dev libxml2 gcc g++ unixodbc-dev

RUN pip install -r requirements.txt

COPY ./project .

RUN python manage.py migrate
RUN python manage.py loaddata doctorList.json

EXPOSE 8000

# CMD gunicorn -w 4 -b 0.0.0.0:8000 project.wsgi:application --log-level debug
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
