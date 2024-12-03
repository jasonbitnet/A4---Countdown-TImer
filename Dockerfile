
FROM python:3.12

WORKDIR /app

ADD main.py .

CMD ["python", "main.py"]
