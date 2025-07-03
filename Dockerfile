#파이썬 버전 : 3.13
FROM python:3.13-slim

#필수 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opensource_app

COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/

WORKDIR /opensource_app/backend

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]