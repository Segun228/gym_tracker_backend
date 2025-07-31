FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


COPY . /app


WORKDIR /app/server/gym_tracker_backend

COPY /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


RUN adduser --system --group appuser
USER appuser


CMD ["gunicorn", "gym_tracker_backend.wsgi:application", "--bind", "0.0.0.0:8000"]