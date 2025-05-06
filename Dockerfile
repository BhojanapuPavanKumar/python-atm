FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt file found"

CMD ["python", "atm.py"]
