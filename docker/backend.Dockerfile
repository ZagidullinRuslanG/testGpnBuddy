FROM python:3.11
WORKDIR /app

# Установка зависимостей
COPY ./src/python/ .
RUN pip install -r requirements.txt
#
# Запуск приложения
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]