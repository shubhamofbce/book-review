# Dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/

COPY . /code/

RUN pip install --no-cache-dir -r requirements.txt

ENV DATABASE_URL postgres://pguser:pgpassword@db:5432/book-review

COPY entrypoint.sh /code/

# Make entrypoint script executable
RUN chmod +x /code/entrypoint.sh

# Set entrypoint
ENTRYPOINT ["/code/entrypoint.sh"]