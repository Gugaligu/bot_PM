# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем supervisord
RUN apt-get update && apt-get install -y supervisor

# Копируем исходный код
COPY . .

# Копируем конфигурацию supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Указываем порт, который будет использовать FastAPI
EXPOSE 8000

# Запускаем supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]