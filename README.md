# SAP SuccessFactors LMS MockServer

Ein vollständiger Mock-Server für die SAP SuccessFactors Learning Management System (LMS) API mit realistischen Mock-Daten und OData v4 Unterstützung.

## Inhaltsverzeichnis

- [Übersicht](#übersicht)
- [Features](#features)
- [Architektur](#architektur)
- [Installation](#installation)
- [Konfiguration](#konfiguration)
- [API-Endpunkte](#api-endpunkte)
- [OData-Unterstützung](#odata-unterstützung)
- [Mock-Daten](#mock-daten)
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
- **Python 3.12** - Runtime Environment

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
├── Dockerfile                 # Docker-Konfiguration
├── docker-compose.yml         # Docker Compose
├── requirements.txt           # Python-Abhängigkeiten
├── LICENSE                    # MIT-Lizenz
└── README.md                  # Diese Dokumentation
```

## Installation

### Voraussetzungen
- Python 3.12 oder höher
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

## API-Endpunkte

### 🔧 System-Endpunkte

#### Health Check
```bash
GET /health
```

#### Root Information
```bash
GET /
```

### 🔄 Partner Extract Services

#### Partner Extract Configuration
```bash
GET /learning/public-api/rest/v1/partnerExtractConfig?partnerID=PARTNER001
PUT /learning/public-api/rest/v1/partnerExtractConfig
```

#### Adhoc Data Extract
```bash
PUT /learning/public-api/rest/v1/adhocDataExtract?partnerID=PARTNER001
```

### 📚 Curriculum Services

#### Admin Curriculum Service
```bash
GET /learning/odatav4/public/admin/curriculum-service/v1/$metadata
GET /learning/odatav4/public/admin/curriculum-service/v1/Curricula
```

#### User Curriculum Service
```bash
GET /learning/odatav4/public/user/curriculum-service/v1/$metadata
GET /learning/odatav4/public/user/curriculum-service/v1/Curricula
```

### 📖 Learning Event Services

#### Admin Learning Event Service
```bash
GET /learning/odatav4/public/admin/learningevent-service/v1/$metadata
POST /learning/odatav4/public/admin/learningevent-service/v1/recordLearningEvents
```

#### User Learning Event Service
```bash
GET /learning/odatav4/public/user/learningevent-service/v1/$metadata
GET /learning/odatav4/public/user/learningevent-service/v1/ExternalLearningEvents
POST /learning/odatav4/public/user/learningevent-service/v1/ExternalLearningEvents
```

### 📋 Learning Plan Service
```bash
GET /learning/odatav4/public/user/learningplan-service/v1/$metadata
GET /learning/odatav4/public/user/learningplan-service/v1/LearningPlans
```

### 🗓️ Scheduled Offering Services

#### Admin Scheduled Offering Service
```bash
GET /learning/odatav4/public/admin/scheduledoffering-service/v1/$metadata
GET /learning/odatav4/public/admin/scheduledoffering-service/v1/ScheduledOfferings
```

#### User Scheduled Offering Service
```bash
GET /learning/odatav4/public/user/scheduledoffering-service/v1/$metadata
GET /learning/odatav4/public/user/scheduledoffering-service/v1/ScheduledOfferings
```

### 🔍 Search Services

#### Admin Search Service
```bash
GET /learning/odatav4/public/admin/search-service/v1/$metadata
GET /learning/odatav4/public/admin/search-service/v1/Programs
GET /learning/odatav4/public/admin/search-service/v1/Students
GET /learning/odatav4/public/admin/search-service/v1/Items
```

### 👥 User Assignment Services

#### v1 User Assignment Service
```bash
GET /learning/odatav4/public/user/userassignment-service/v1/$metadata
GET /learning/odatav4/public/user/userassignment-service/v1/UserPrograms
```

#### v2 User Assignment Service
```bash
GET /learning/odatav4/public/user/userassignment-service/v2/$metadata
POST /learning/odatav4/public/user/userassignment-service/v2/itemAssignments
POST /learning/odatav4/public/user/userassignment-service/v2/removeItemAssignments
```

### 📊 User Learning Service
```bash
GET /learning/odatav4/public/user/userlearning-service/v1/$metadata
GET /learning/odatav4/public/user/userlearning-service/v1/LearningHistories
```

### 👤 User Services

#### Admin User Services
```bash
GET /learning/odatav4/public/admin/user-service/v1/$metadata
GET /learning/odatav4/public/admin/user-service/v2/$metadata
POST /learning/odatav4/public/admin/user-service/v2/MergeUsers
GET /learning/odatav4/public/admin/user-service/v2/Users
```

#### User Services
```bash
GET /learning/odatav4/public/user/user-service/v1/$metadata
GET /learning/odatav4/public/user/user-service/v1/Approvals
GET /learning/odatav4/public/user/user-service/v2/$metadata
GET /learning/odatav4/public/user/user-service/v2/UserAssignments
```

### 🛒 Catalog Services

#### Catalog Search
```bash
GET /learning/odatav4/catalogSearch/v1/$metadata
GET /learning/odatav4/catalogSearch/v1/CatalogItems
```

#### User Catalog Search
```bash
GET /learning/odatav4/public/user/catalogSearch/v1/$metadata
GET /learning/odatav4/public/user/catalogSearch/v1/CatalogItems
```

#### Admin Catalog Service
```bash
GET /learning/odatav4/public/admin/catalog-service/v1/$metadata
GET /learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed
GET /learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/{catalogId}/CoursesFeed
GET /learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/{catalogId}/CurriculaFeed
GET /learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/{catalogId}/ProgramsFeed
GET /learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/{catalogId}/CollectionsFeed
```

### 💰 Financial Transactions Service
```bash
GET /learning/odatav4/public/admin/financialtransactions/v1/$metadata
GET /learning/odatav4/public/admin/financialtransactions/v1/FinancialTransactions
```

## OData-Unterstützung

### Unterstützte Query-Parameter

| Parameter | Beschreibung | Beispiel |
|-----------|-------------|----------|
| `$filter` | Filterung der Ergebnisse | `status eq 'Active'` |
| `$select` | Auswahl spezifischer Felder | `curriculumID,title,status` |
| `$expand` | Erweitern verwandter Entitäten | `items` |
| `$orderby` | Sortierung der Ergebnisse | `title asc` |
| `$top` | Begrenzung der Anzahl Ergebnisse | `10` |
| `$skip` | Überspringen von Ergebnissen | `20` |
| `$count` | Anzahl der Ergebnisse einschließen | `true` |

### Beispiel OData-Queries

```bash
# Top 5 Curricula abrufen
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$top=5"

# Curricula mit Count abrufen
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$count=true"

# Spezifische Felder auswählen
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$select=curriculumID,title,status"

# Aktive Curricula filtern
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$filter=status eq 'Active'"

# Kombinierte Query
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$filter=status eq 'Active'&\$select=curriculumID,title&\$top=10"
```

## Mock-Daten

### Datenstruktur

Alle Mock-Daten sind in separaten JSON-Dateien im `src/mock_data/` Verzeichnis organisiert:

#### Curriculum-Daten (`catalog_curricula.json`)
```json
{
  "@odata.context": "$metadata#CurriculaFeed",
  "value": [
    {
      "curriculumID": "CURR_001",
      "title": "Management Development Program",
      "description": "Comprehensive management development curriculum",
      "category": "Leadership",
      "difficulty": "Intermediate",
      "totalDuration": 40.0,
      "totalItems": 5,
      "status": "Active",
      "items": [...]
    }
  ]
}
```

#### Kurs-Daten (`catalog_courses.json`)
```json
{
  "@odata.context": "$metadata#CoursesFeed",
  "value": [
    {
      "courseID": "COURSE_001",
      "title": "Leadership Fundamentals",
      "description": "Essential leadership skills for new managers",
      "category": "Leadership",
      "difficulty": "Beginner",
      "duration": 8.0,
      "language": "English",
      "status": "Active"
    }
  ]
}
```

### Daten-Konsistenz

✅ **Konsistente Eigenschaften:**
- Alle IDs sind konsistent zwischen verschiedenen Endpunkten
- Realistische Zeitstempel und Daten
- Logische Beziehungen zwischen Entitäten
- Verschiedene Status-Werte für realistische Szenarien

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

# Curriculum Data
curl -X GET "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula"
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

@sap_lms_bp.route('/new/endpoint/v1/Data', methods=['GET'])
def new_endpoint_data():
    """Get new endpoint data"""
    query_params = parse_odata_query(request)
    data = load_mock_data('new_endpoint_data.json')
    
    return jsonify(create_odata_response(
        data.get('value', []),
        "$metadata#Data",
        len(data.get('value', [])) if query_params['count'] else None
    ))
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
- **Dokumentation:** Detaillierte API-Informationen in [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
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

**📅 Letzte Aktualisierung:** Juli 2025 | **🏷️ Version:** 1.0.0

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](Dockerfile)

</div>
```