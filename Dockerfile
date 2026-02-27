FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y default-mysql-client \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
