FROM python

# ENV DEBIAN_FRONTEND=noninteractive

# RUN apt-get update
# RUN apt-get install -y python3 python3-pip libpq-dev
# RUN apt-get install -y tzdata
# RUN apt-get install -y python3-venv
# RUN apt-get clean

# RUN python3 -m venv /opt/venv

# ENV PATH="/opt/venv/bin:$PATH"

# RUN pip install --upgrade pip

# ENV TZ=UTC

WORKDIR /app

# Скопировать файл requirements.txt
COPY requirements.txt .

# Установить зависимости
RUN pip install -r requirements.txt

COPY . .

EXPOSE 9000

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:9000"]
