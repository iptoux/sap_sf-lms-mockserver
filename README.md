<div align="center">
<h1>SAP SuccessFactors LMS MockServer</h1>

**📅 Letzte Aktualisierung:** Juli 2025 | **🏷️ Version:** 1.0.0

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](Dockerfile)

</div>

Ein vollständiger Mock-Server für die SAP SuccessFactors Learning Management System (LMS) API mit realistischen Mock-Daten und OData v4 Unterstützung.

## Inhaltsverzeichnis

- [Übersicht](#übersicht)
- [Features](#features)
- [Architektur](#architektur)
- [Installation](#installation)
- [Konfiguration](#konfiguration)
- [API-Dokumentation](#api-dokumentation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Docker](#docker)
- [Anpassung](#anpassung)
- [Troubleshooting](#troubleshooting)
- [Beitragen](#beitragen)
- [Lizenz](#lizenz)
- [Support](#support)
- [Changelog](#changelog)

## Übersicht

Der SAP SuccessFactors LMS MockServer ist eine vollständige Implementierung eines Mock-Servers, der die SAP SuccessFactors Learning Management System (LMS) API emuliert. Dieser Server wurde basierend auf der offiziellen SAP SuccessFactors Learning OData APIs Dokumentation entwickelt und unterstützt alle 36 dokumentierten API-Endpunkte mit realistischen Mock-Daten.

**Basis-URL:** `http://localhost:5001`

## Features

### 🚀 Vollständige API-Abdeckung
- **36 API-Endpunkte** vollständig implementiert
- **OData v4** konforme Responses
- **REST API** Endpunkte für Partner-Integration
- **Metadata-Endpunkte** für alle Services
- **CRUD-Operationen** für Daten-Endpunkte

### 📊 Realistische Mock-Daten
- Separate JSON-Dateien für jeden Endpunkt
- Strukturierte Daten entsprechend der API-Spezifikation
- Realistische Beispieldaten für bessere Tests
- Konsistente Datenbeziehungen zwischen Endpunkten

### 🛠️ Entwicklerfreundlich
- **CORS-Unterstützung** für Frontend-Integration
- **Detaillierte Logging** für Debugging
- **Flexible Konfiguration** über Umgebungsvariablen
- **Docker-ready** für einfache Bereitstellung

## Architektur

### Technologie-Stack
- **Flask** - Python Web Framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **SQLAlchemy** - Database ORM
- **JSON** - Mock-Daten-Storage
- **Python 3.13** - Runtime Environment

### Projektstruktur
```
sap-lms-mockserver/
├── src/
│   ├── main.py                 # Hauptanwendung
│   ├── routes/
│   │   ├── user.py            # Beispiel-Routen
│   │   └── sap_lms_api.py     # SAP LMS API Routen
│   ├── models/
│   │   └── user.py            # Datenmodelle
│   ├── mock_data/             # Mock-Daten-Dateien
│   │   ├── partner_extract_config.json
│   │   ├── admin_curriculum_service_metadata.json
│   │   ├── catalog_courses.json
│   │   └── ... (weitere 30+ Dateien)
│   ├── database/              # SQLite-Datenbank
│   └── static/                # Statische Dateien
├── docs/                      # Dokumentation
│   └── API_DOCUMENTATION.md   # Detaillierte API-Dokumentation
├── Dockerfile                 # Docker-Konfiguration
├── docker-compose.yml         # Docker Compose
├── requirements.txt           # Python-Abhängigkeiten
├── LICENSE                    # MIT-Lizenz
└── README.md                  # Projekt-Dokumentation
```

## Installation

### Voraussetzungen
- Python 3.13 oder höher
- pip (Python Package Manager)
- Git (für Klonen des Repositories)

### 🐍 Lokale Installation

1. **Repository klonen**
   ```bash
   git clone <repository-url>
   cd sap-lms-mockserver
   ```

2. **Virtuelle Umgebung erstellen und aktivieren**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # oder
   venv\Scripts\activate     # Windows
   ```

3. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

4. **Server starten**
   ```bash
   python src/main.py
   ```

Der Server läuft standardmäßig auf `http://localhost:5001`

### 🐳 Docker Installation

```bash
# Docker Image erstellen
docker build -t sap-lms-mockserver .

# Container starten
docker run -p 5001:5001 sap-lms-mockserver

# Oder mit Docker Compose
docker-compose up -d
```

## Konfiguration

### Umgebungsvariablen
| Variable | Beschreibung | Standard |
|----------|-------------|----------|
| `FLASK_ENV` | Umgebung (development/production) | `production` |
| `FLASK_DEBUG` | Debug-Modus | `False` |
| `PORT` | Server-Port | `5001` |
| `HOST` | Server-Host | `0.0.0.0` |

### Beispiel .env Datei
```env
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5001
HOST=0.0.0.0
```

## API-Dokumentation

Eine detaillierte API-Dokumentation mit allen Endpunkten, Parametern und Beispielen finden Sie in der [**API_DOCUMENTATION.md**](docs/API_DOCUMENTATION.md).

### 🔧 Schnellstart - Wichtige Endpunkte

#### Health Check
```bash
curl -X GET http://localhost:5001/health
```

#### Partner Extract Configuration
```bash
curl -X GET "http://localhost:5001/learning/public-api/rest/v1/partnerExtractConfig?partnerID=PARTNER001"
```

#### Curriculum Service
```bash
curl -X GET "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula"
```

### 📚 API-Kategorien

- **System-Endpunkte** - Health Check, Root Information
- **Partner Extract Services** - Konfiguration und Datenextraktion
- **Curriculum Services** - Admin und User Curriculum Management
- **Learning Event Services** - Lernereignisse und externe Events
- **Scheduled Offering Services** - Geplante Kursangebote
- **Search Services** - Suche nach Programmen, Studenten und Items
- **User Assignment Services** - Benutzer-Zuweisungen (v1 und v2)
- **User Learning Service** - Lernhistorie und Fortschritte
- **User Services** - Benutzerverwaltung und Genehmigungen
- **Catalog Services** - Katalogsuche und -verwaltung
- **Financial Transactions** - Finanztransaktionen

### 🔍 OData v4 Unterstützung

Der Server unterstützt alle wichtigen OData v4 Query-Parameter:

- `$filter` - Filterung der Ergebnisse
- `$select` - Auswahl spezifischer Felder
- `$expand` - Erweitern verwandter Entitäten
- `$orderby` - Sortierung der Ergebnisse
- `$top` - Begrenzung der Anzahl Ergebnisse
- `$skip` - Überspringen von Ergebnissen
- `$count` - Anzahl der Ergebnisse einschließen

**Beispiel:**
```bash
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$filter=status eq 'Active'&\$select=curriculumID,title&\$top=10"
```

## Testing

### 🧪 Manuelle Tests

#### cURL-Beispiele
```bash
# Health Check
curl -X GET http://localhost:5001/health

# Partner Extract Config
curl -X GET "http://localhost:5001/learning/public-api/rest/v1/partnerExtractConfig?partnerID=PARTNER001"

# Curriculum Metadata
curl -X GET "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/\$metadata"
```

#### Browser-Tests
Einfache GET-Endpunkte können direkt im Browser getestet werden:
- `http://localhost:5001/health`
- `http://localhost:5001/`
- `http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/$metadata`

### 🔬 Automatisierte Tests

```python
import unittest
import requests

class TestSAPLMSMockServer(unittest.TestCase):
    BASE_URL = "http://localhost:5001"
    
    def test_health_check(self):
        response = requests.get(f"{self.BASE_URL}/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")
    
    def test_partner_extract_config(self):
        response = requests.get(
            f"{self.BASE_URL}/learning/public-api/rest/v1/partnerExtractConfig",
            params={"partnerID": "PARTNER001"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["restOperationStatusVOX"]["status"], "SUCCESS")
```

## Deployment

### 🖥️ Lokale Entwicklung
```bash
# Entwicklungsserver starten
python src/main.py
```

### 🏭 Produktions-Deployment

#### Mit Gunicorn
```bash
# Gunicorn installieren
pip install gunicorn

# Server mit Gunicorn starten
gunicorn --bind 0.0.0.0:5001 --workers 4 src.main:app
```

#### Mit systemd (Linux)
```ini
# /etc/systemd/system/sap-lms-mockserver.service
[Unit]
Description=SAP LMS MockServer
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/sap-lms-mockserver
ExecStart=/opt/sap-lms-mockserver/venv/bin/gunicorn --bind 0.0.0.0:5001 --workers 4 src.main:app
Restart=always

[Install]
WantedBy=multi-user.target
```

## Docker

### 🐳 Docker-Befehle

```bash
# Image erstellen
docker build -t sap-lms-mockserver .

# Container starten
docker run -p 5001:5001 sap-lms-mockserver

# Container im Hintergrund ausführen
docker run -d -p 5001:5001 --name sap-lms-server sap-lms-mockserver

# Container-Logs anzeigen
docker logs sap-lms-server

# Container stoppen
docker stop sap-lms-server
```

### Docker Compose

```yaml
version: '3.8'

services:
  sap-lms-mockserver:
    build: .
    ports:
      - "5001:5001"
    environment:
      - FLASK_ENV=production
      - FLASK_DEBUG=False
    volumes:
      - ./src/database:/app/src/database
    restart: unless-stopped
```

```bash
# Service starten
docker-compose up -d

# Service stoppen
docker-compose down

# Logs anzeigen
docker-compose logs -f
```

## Anpassung

### 🛠️ Mock-Daten anpassen

Mock-Daten können einfach durch Bearbeitung der JSON-Dateien im `src/mock_data/` Verzeichnis angepasst werden:

1. **Neue Daten hinzufügen:** Neue Objekte zu den Arrays hinzufügen
2. **Bestehende Daten ändern:** Werte in den JSON-Objekten modifizieren
3. **Neue Endpunkte:** Neue JSON-Dateien erstellen und entsprechende Routen hinzufügen

### 🔧 Neue Endpunkte hinzufügen

```python
@sap_lms_bp.route('/new/endpoint/v1/$metadata', methods=['GET'])
def new_endpoint_metadata():
    """Get new endpoint metadata"""
    data = load_mock_data('new_endpoint_metadata.json')
    return jsonify(data)
```

### 📝 Logging konfigurieren

```python
import logging

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## Troubleshooting

### 🚨 Häufige Probleme

#### Port bereits belegt
```bash
# Anderen Port verwenden
python src/main.py --port 5002

# Prozess auf Port 5001 finden und beenden
lsof -ti:5001 | xargs kill -9
```

#### CORS-Fehler
```python
# CORS für spezifische Origins konfigurieren
CORS(app, origins=['http://localhost:3000', 'http://localhost:8080'])
```

#### Mock-Daten nicht gefunden
```bash
# Überprüfen, ob Dateien existieren
ls src/mock_data/

# Pfade in load_mock_data() überprüfen
```

#### Virtuelle Umgebung Probleme
```bash
# Neue virtuelle Umgebung erstellen
python -m venv new_venv
source new_venv/bin/activate
pip install -r requirements.txt
```

### 🔍 Debug-Modus

```python
# Debug-Informationen aktivieren
app.run(host='0.0.0.0', port=5001, debug=True)

# Detaillierte Logs
import logging
logging.getLogger('flask').setLevel(logging.DEBUG)
```

## Beitragen

### 👥 Entwicklungsrichtlinien

1. **Code-Stil:** PEP 8 befolgen
2. **Dokumentation:** Alle neuen Funktionen dokumentieren
3. **Tests:** Tests für neue Endpunkte hinzufügen
4. **Mock-Daten:** Realistische und konsistente Daten verwenden

### 🔀 Pull Requests

1. Fork des Repositories erstellen
2. Feature-Branch erstellen (`git checkout -b feature/amazing-feature`)
3. Änderungen committen (`git commit -m 'Add amazing feature'`)
4. Branch pushen (`git push origin feature/amazing-feature`)
5. Pull Request erstellen

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe [LICENSE](LICENSE) für Details.

## Support

### 📞 Hilfe und Unterstützung

- **GitHub Issues:** Bug-Reports und Feature-Requests
- **API-Dokumentation:** Detaillierte Endpunkt-Informationen in [API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)
- **Community:** Diskussionen über GitHub Discussions

### 🆘 Schnelle Hilfe

| Problem | Lösung |
|---------|--------|
| Server startet nicht | Port-Konflikt prüfen, Dependencies installieren |
| API-Antworten fehlerhaft | Mock-Daten validieren, Logs prüfen |
| CORS-Probleme | CORS-Konfiguration anpassen |
| Docker-Probleme | Dockerfile und docker-compose.yml prüfen |

## Changelog

### 📋 Version 1.0.0 (Juli 2025)
- ✅ Initiale Implementierung aller 36 SAP LMS API Endpunkte
- ✅ Vollständige OData v4 Unterstützung
- ✅ Realistische Mock-Daten für alle Services
- ✅ CORS-Unterstützung für Frontend-Integration
- ✅ Docker-Unterstützung
- ✅ Umfassende Dokumentation und Beispiele
- ✅ SQLAlchemy-Integration für Datenpersistenz
- ✅ Automatisierte Tests und CI/CD-Pipeline

---

<div align="center">

**🔧 Entwickelt mit Unterstützung von [Manus AI](https://manus.im)**

</div>