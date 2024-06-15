FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 python3-pip libpq-dev
RUN apt-get install tzdata
RUN apt-get clean

ENV TZ=UTC

WORKDIR /app

# Скопировать файл requirements.txt
COPY requirements.txt .

# Установить зависимости
RUN pip install -r requirements.txt

COPY . .

EXPOSE 9000

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:9000"]
