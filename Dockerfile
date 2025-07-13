FROM python:3.11

RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /code

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
