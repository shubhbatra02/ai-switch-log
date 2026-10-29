FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY db_check.py .
CMD ["python","db_check.py"]

