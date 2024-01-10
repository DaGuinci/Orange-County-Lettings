FROM python:3.10 AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app
RUN python manage.py collectstatic --noinput
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
