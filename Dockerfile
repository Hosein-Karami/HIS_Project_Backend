FROM python:3.9.18-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./project .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
