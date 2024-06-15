FROM python

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose the port the gRPC service will run on
EXPOSE 3092 3094

ENTRYPOINT ["/app/entrypoint.sh"]

# Command to run the gRPC service
CMD ["python3", "listener.py"]