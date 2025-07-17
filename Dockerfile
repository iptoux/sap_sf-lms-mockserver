# Verwende die neueste Python-Version (3.12) als Basis-Image
FROM python:3.13-slim

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere requirements.txt zuerst für bessere Layer-Caching
COPY requirements.txt .

# Installiere Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Quellcode
COPY src/ ./src/

# Erstelle das database-Verzeichnis für SQLite
RUN mkdir -p src/database

# Exponiere den Port 5001
EXPOSE 5001

# Setze Umgebungsvariablen
ENV FLASK_ENV=production
ENV FLASK_DEBUG=False
ENV PYTHONPATH=/app

# Starte die Anwendung
CMD ["python", "src/main.py"]