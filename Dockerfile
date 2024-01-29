FROM python:3.9.18-slim

RUN apt update && apt install -y curl

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY project app

RUN python manage.py migrate
RUN python manage.py loaddata doctorList.json

EXPOSE 80

CMD gunicorn -w 4 -b 0.0.0.0:80 project.wsgi:application --log-level debug
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
