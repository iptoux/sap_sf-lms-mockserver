# SAP SuccessFactors LMS MockServer

## Übersicht

Der SAP SuccessFactors LMS MockServer ist eine vollständige Implementierung eines Mock-Servers, der die SAP SuccessFactors Learning Management System (LMS) API emuliert. Dieser Server wurde basierend auf der offiziellen SAP SuccessFactors Learning OData APIs Dokumentation entwickelt und unterstützt alle 36 dokumentierten API-Endpunkte mit realistischen Mock-Daten.

## Funktionen

### Vollständige API-Abdeckung
- **36 API-Endpunkte** vollständig implementiert
- **OData v4** konforme Responses
- **REST API** Endpunkte für Partner-Integration
- **Metadata-Endpunkte** für alle Services
- **Daten-Endpunkte** mit CRUD-Operationen

### Realistische Mock-Daten
- Separate JSON-Dateien für jeden Endpunkt
- Strukturierte Daten entsprechend der API-Spezifikation
- Realistische Beispieldaten für bessere Tests
- Konsistente Datenbeziehungen zwischen Endpunkten

### Entwicklerfreundlich
- **CORS-Unterstützung** für Frontend-Integration
- **Detaillierte Logging** für Debugging
- **Flexible Konfiguration** über Umgebungsvariablen
- **Docker-ready** für einfache Bereitstellung

## Architektur

### Technologie-Stack
- **Flask** - Python Web Framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **JSON** - Mock-Daten-Storage
- **Python 3.11** - Runtime Environment

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
│   └── static/                # Statische Dateien
├── venv/                      # Virtuelle Umgebung
├── requirements.txt           # Python-Abhängigkeiten
└── README.md                  # Diese Dokumentation
```

## Installation und Setup

### Voraussetzungen
- Python 3.11 oder höher
- pip (Python Package Manager)
- Git (für Klonen des Repositories)

### Schritt-für-Schritt Installation

1. **Repository klonen**
```bash
git clone <repository-url>
cd sap-lms-mockserver
```

2. **Virtuelle Umgebung aktivieren**
```bash
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

### Konfiguration

#### Umgebungsvariablen
- `FLASK_ENV` - Umgebung (development/production)
- `FLASK_DEBUG` - Debug-Modus (True/False)
- `PORT` - Server-Port (Standard: 5001)
- `HOST` - Server-Host (Standard: 0.0.0.0)

#### Beispiel .env Datei
```env
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5001
HOST=0.0.0.0
```

## API-Endpunkte

### 1. Partner Extract Configuration
**Endpunkt:** `/learning/public-api/rest/v1/partnerExtractConfig`

**Methoden:** GET, PUT

**Beschreibung:** Konfiguration für Partner-Datenextraktion

**Beispiel Request:**
```bash
curl -X GET "http://localhost:5001/learning/public-api/rest/v1/partnerExtractConfig?partnerID=PARTNER001"
```

**Beispiel Response:**
```json
{
  "restOperationStatusVOX": {
    "operation": null,
    "status": "SUCCESS",
    "data": {
      "sftpPath": "/customer/subfolder/path",
      "partnerID": "PARTNER001",
      "enabled": true,
      "email": "partner@example.com",
      "keyOwner": "SAP_LMS_ADMIN",
      "encryptionKey": "AES256_ENCRYPTION_KEY_PLACEHOLDER",
      "lastExtractDate": "2024-01-15T10:30:00Z",
      "extractFrequency": "DAILY"
    }
  },
  "errors": null,
  "warnings": null
}
```

### 2. Adhoc Data Extract
**Endpunkt:** `/learning/public-api/rest/v1/adhocDataExtract`

**Methoden:** PUT

**Beschreibung:** Erstellt eine Ad-hoc-Datenextraktion

### 3. Admin Curriculum Service
**Basis-URL:** `/learning/odatav4/public/admin/curriculum-service/v1`

**Endpunkte:**
- `/$metadata` - Service-Metadaten
- `/Curricula` - Curriculum-Daten (GET)

**Beispiel Request:**
```bash
curl -X GET "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula"
```

### 4. User Curriculum Service
**Basis-URL:** `/learning/odatav4/public/user/curriculum-service/v1`

**Endpunkte:**
- `/$metadata` - Service-Metadaten
- `/Curricula` - Benutzer-spezifische Curriculum-Daten

### 5. Learning Event Services
**Admin:** `/learning/odatav4/public/admin/learningevent-service/v1`
**User:** `/learning/odatav4/public/user/learningevent-service/v1`

**Funktionen:**
- Aufzeichnung von Lernereignissen
- Externe Lernereignisse verwalten
- Lernhistorie abrufen

### 6. Learning Plan Service
**Basis-URL:** `/learning/odatav4/public/user/learningplan-service/v1`

**Endpunkte:**
- `/$metadata` - Service-Metadaten
- `/LearningPlans` - Lernpläne abrufen

### 7. Scheduled Offering Services
**Admin:** `/learning/odatav4/public/admin/scheduledoffering-service/v1`
**User:** `/learning/odatav4/public/user/scheduledoffering-service/v1`

**Funktionen:**
- Geplante Kursangebote verwalten
- Anmeldungen verwalten
- Teilnehmerlisten abrufen

### 8. Search Services
**Admin:** `/learning/odatav4/public/admin/search-service/v1`

**Endpunkte:**
- `/Programs` - Programme suchen
- `/Students` - Studenten suchen
- `/Items` - Lernelemente suchen

### 9. User Assignment Services
**v1:** `/learning/odatav4/public/user/userassignment-service/v1`
**v2:** `/learning/odatav4/public/user/userassignment-service/v2`

**Funktionen:**
- Benutzer-Zuweisungen verwalten
- Programm-Zuweisungen
- Element-Zuweisungen

### 10. User Learning Service
**Basis-URL:** `/learning/odatav4/public/user/userlearning-service/v1`

**Endpunkte:**
- `/LearningHistories` - Lernhistorie abrufen
- `/learninghistorys` - Einzelne Lernhistorie-Einträge

### 11. User Services
**Admin v1:** `/learning/odatav4/public/admin/user-service/v1`
**Admin v2:** `/learning/odatav4/public/admin/user-service/v2`
**User v1:** `/learning/odatav4/public/user/user-service/v1`
**User v2:** `/learning/odatav4/public/user/user-service/v2`

**Funktionen:**
- Benutzerverwaltung
- Benutzer-Zusammenführung
- Genehmigungen verwalten

### 12. Catalog Services
**Search:** `/learning/odatav4/catalogSearch/v1`
**User Search:** `/learning/odatav4/public/user/catalogSearch/v1`
**Admin Catalog:** `/learning/odatav4/public/admin/catalog-service/v1`

**Funktionen:**
- Katalog durchsuchen
- Kurse, Curricula, Programme abrufen
- Sammlungen verwalten

### 13. Financial Transactions
**Basis-URL:** `/learning/odatav4/public/admin/financialtransactions/v1`

**Endpunkte:**
- `/$metadata` - Service-Metadaten
- `/FinancialTransactions` - Finanztransaktionen abrufen

## OData-Unterstützung

### Unterstützte Query-Parameter
- `$filter` - Filterung der Ergebnisse
- `$select` - Auswahl spezifischer Felder
- `$expand` - Erweitern verwandter Entitäten
- `$orderby` - Sortierung der Ergebnisse
- `$top` - Begrenzung der Anzahl Ergebnisse
- `$skip` - Überspringen von Ergebnissen
- `$count` - Anzahl der Ergebnisse einschließen

### Beispiel OData-Queries
```bash
# Top 5 Curricula abrufen
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$top=5"

# Curricula mit Count abrufen
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$count=true"

# Spezifische Felder auswählen
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$select=curriculumID,title,status"
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
- Alle IDs sind konsistent zwischen verschiedenen Endpunkten
- Realistische Zeitstempel und Daten
- Logische Beziehungen zwischen Entitäten
- Verschiedene Status-Werte für realistische Szenarien

## Testing

### Manuelle Tests
Der Server kann mit verschiedenen Tools getestet werden:

#### cURL
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

#### Postman
Eine Postman-Collection kann erstellt werden mit allen verfügbaren Endpunkten für systematische Tests.

#### Browser
Einfache GET-Endpunkte können direkt im Browser getestet werden:
- `http://localhost:5001/health`
- `http://localhost:5001/`
- `http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/$metadata`

### Automatisierte Tests
Für Produktionsumgebungen sollten automatisierte Tests implementiert werden:

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

### Lokale Entwicklung
```bash
# Entwicklungsserver starten
python src/main.py
```

### Docker Deployment
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/
COPY venv/ ./venv/

EXPOSE 5001
CMD ["python", "src/main.py"]
```

### Produktions-Deployment
Für Produktionsumgebungen sollte ein WSGI-Server wie Gunicorn verwendet werden:

```bash
# Gunicorn installieren
pip install gunicorn

# Server mit Gunicorn starten
gunicorn --bind 0.0.0.0:5001 --workers 4 src.main:app
```

## Konfiguration und Anpassung

### Mock-Daten anpassen
Mock-Daten können einfach durch Bearbeitung der JSON-Dateien im `src/mock_data/` Verzeichnis angepasst werden:

1. **Neue Daten hinzufügen:** Einfach neue Objekte zu den Arrays hinzufügen
2. **Bestehende Daten ändern:** Werte in den JSON-Objekten modifizieren
3. **Neue Endpunkte:** Neue JSON-Dateien erstellen und entsprechende Routen hinzufügen

### Neue Endpunkte hinzufügen
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

### Logging konfigurieren
```python
import logging

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# In Routen verwenden
@sap_lms_bp.route('/endpoint', methods=['GET'])
def endpoint():
    logging.info(f"Request received for endpoint: {request.url}")
    # ... Rest der Implementierung
```

## Troubleshooting

### Häufige Probleme

#### Port bereits belegt
```bash
# Anderen Port verwenden
python src/main.py --port 5002

# Oder in main.py ändern
app.run(host='0.0.0.0', port=5002, debug=True)
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

### Debug-Modus
```python
# Debug-Informationen aktivieren
app.run(host='0.0.0.0', port=5001, debug=True)

# Detaillierte Logs
import logging
logging.getLogger('flask').setLevel(logging.DEBUG)
```

## Beitragen

### Entwicklungsrichtlinien
1. **Code-Stil:** PEP 8 befolgen
2. **Dokumentation:** Alle neuen Funktionen dokumentieren
3. **Tests:** Tests für neue Endpunkte hinzufügen
4. **Mock-Daten:** Realistische und konsistente Daten verwenden

### Pull Requests
1. Fork des Repositories erstellen
2. Feature-Branch erstellen
3. Änderungen implementieren und testen
4. Pull Request mit detaillierter Beschreibung erstellen

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe LICENSE-Datei für Details.

## Support

Für Fragen und Support:
- GitHub Issues für Bug-Reports und Feature-Requests
- Dokumentation für detaillierte API-Informationen
- Community-Forum für allgemeine Diskussionen

## Changelog

### Version 1.0.0
- Initiale Implementierung aller 36 SAP LMS API Endpunkte
- Vollständige OData v4 Unterstützung
- Realistische Mock-Daten für alle Services
- CORS-Unterstützung für Frontend-Integration
- Umfassende Dokumentation und Beispiele

---

**Entwickelt mit unterstützung von:** [Manus AI](https://manus.im/share/YghKPlSx6ybOlVYdnJJ7cY?replay=1)  
**Letzte Aktualisierung:** Juli 2025
**Version:** 1.0.0

