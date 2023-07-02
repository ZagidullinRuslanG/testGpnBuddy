FROM python:3.11
WORKDIR /app

# Установка зависимостей
COPY . .
RUN pip install -r requirements.txt
#
# Запуск приложения
CMD ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]