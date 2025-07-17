# SAP SuccessFactors LMS MockServer - API Dokumentation

**Version:** 1.0.0  
**Letzte Aktualisierung:** Juli 2025  
**Entwickelt mit Unterstützung durch:** Manus AI  

---
## Inhaltsverzeichnis

1.  [Übersicht](#1-übersicht)
2.  [Schnellstart](#2-schnellstart)
3.  [REST API Endpunkte](#3-rest-api-endpunkte)
    *   [3.1. System-Endpunkte](#31-system-endpunkte)
    *   [3.2. Partner Extract Configuration](#32-partner-extract-configuration)
    *   [3.3. Adhoc Data Extract](#33-adhoc-data-extract)
4.  [OData v4 Services](#4-odata-v4-services)
    *   [4.1. Curriculum Services](#41-curriculum-services)
    *   [4.2. Learning Event Services](#42-learning-event-services)
    *   [4.3. Learning Plan Service](#43-learning-plan-service)
    *   [4.4. Scheduled Offering Services](#44-scheduled-offering-services)
    *   [4.5. Search Services](#45-search-services)
    *   [4.6. User Assignment Services](#46-user-assignment-services)
    *   [4.7. User Learning Service](#47-user-learning-service)
    *   [4.8. User Services](#48-user-services)
    *   [4.9. Catalog Services](#49-catalog-services)
    *   [4.10. Financial Transactions Service](#410-financial-transactions-service)
5.  [Datenmodelle](#5-datenmodelle)
6.  [Fehlerbehandlung](#6-fehlerbehandlung)
7.  [Workflows & Beispiele](#7-workflows--beispiele)

---

## 1. Übersicht

Diese Dokumentation beschreibt alle verfügbaren API-Endpunkte des SAP SuccessFactors LMS MockServers. Der Server emuliert die vollständige SAP SuccessFactors Learning Management System API mit realistischen Mock-Daten und ermöglicht so eine effiziente Entwicklung und Integration.

- **Basis-URL:** `http://localhost:5001`
- **Unterstützte Formate:** JSON (Standard), OData v4
- **CORS:** Aktiviert für alle Origins
- **Authentifizierung:** Keine erforderlich (im Gegensatz zur echten SAP SF Umgebung)

---

## 2. Schnellstart

Um den Server zu testen, führen Sie den folgenden Health-Check-Befehl aus:

```bash
curl -X GET http://localhost:5001/health
```

Sie sollten eine `200 OK` Antwort mit dem folgenden Body erhalten:

```json
{
  "status": "healthy",
  "service": "SAP SuccessFactors LMS MockServer"
}
```

---

## 3. REST API Endpunkte

### 3.1. System-Endpunkte

#### Root Information

- **GET /**
- **Beschreibung:** Gibt grundlegende Informationen über den Service zurück.
- **Response:**
  ```json
  {
    "service": "SAP SuccessFactors LMS MockServer",
    "version": "1.0.0",
    "description": "Mock server for SAP SuccessFactors Learning Management System API",
    "endpoints": "See documentation for available endpoints"
  }
  ```

#### Health Check

- **GET /health**
- **Beschreibung:** Überprüft den Status des Servers.
- **Response:**
  ```json
  {
    "status": "healthy",
    "service": "SAP SuccessFactors LMS MockServer"
  }
  ```

### 3.2. Partner Extract Configuration

#### Konfiguration abrufen

- **GET /learning/public-api/rest/v1/partnerExtractConfig**
- **Beschreibung:** Ruft die Konfiguration für einen Partner-Datenextrakt ab.
- **Query-Parameter:**
  - `partnerID` (string, **required**): Die ID des Partners.
- **Beispiel-Request:**
  ```bash
  curl -X GET "http://localhost:5001/learning/public-api/rest/v1/partnerExtractConfig?partnerID=PARTNER001"
  ```
- **Beispiel-Response:**
  ```json
  {
    "restOperationStatusVOX": {
      "status": "SUCCESS",
      "data": {
        "sftpPath": "/customer/subfolder/path",
        "partnerID": "PARTNER001",
        "enabled": true,
        "email": "partner@example.com",
        "keyOwner": "SAP_LMS_ADMIN",
        "encryptionKey": "AES256_ENCRYPTION_KEY_PLACEHOLDER",
        "lastExtractDate": "2024-01-15T10:30:00Z",
        "extractFrequency": "DAILY",
        "configuration": {
          "includeUserData": true,
          "includeCourseData": true,
          "includeCurriculumData": true,
          "includeCompletionData": true,
          "dataFormat": "JSON",
          "compression": "GZIP"
        }
      }
    }
  }
  ```

#### Konfiguration aktualisieren

- **PUT /learning/public-api/rest/v1/partnerExtractConfig**
- **Beschreibung:** Aktualisiert die Konfiguration für einen Partner-Datenextrakt.
- **Request Body:**
  ```json
  {
    "partnerID": "PARTNER001",
    "sftpPath": "/customer/subfolder/path",
    "enabled": true,
    "email": "partner@example.com",
    "extractFrequency": "DAILY"
  }
  ```

### 3.3. Adhoc Data Extract

#### Adhoc-Datenextrakt erstellen

- **PUT /learning/public-api/rest/v1/adhocDataExtract**
- **Beschreibung:** Startet einen Adhoc-Datenextrakt.
- **Query-Parameter:**
  - `partnerID` (string, **required**): Die ID des Partners.
- **Request Body:**
  ```json
  {
    "extractType": "FULL",
    "dataTypes": ["USERS", "COURSES", "COMPLETIONS"],
    "dateRange": {
      "startDate": "2024-01-01T00:00:00Z",
      "endDate": "2024-01-31T23:59:59Z"
    }
  }
  ```
- **Response:**
  ```json
  {
    "restOperationStatusVOX": {
      "operation": "ADHOC_EXTRACT",
      "status": "SUCCESS"
    }
  }
  ```

---

## 4. OData v4 Services

Die OData-Services bieten erweiterte Abfragemöglichkeiten.

**Unterstützte Query-Parameter:**
- `$top`: Anzahl der zurückzugebenden Einträge.
- `$skip`: Anzahl der zu überspringenden Einträge.
- `$count`: Gesamtanzahl der Einträge in die Antwort einschließen.
- `$filter`: Datensätze basierend auf Bedingungen filtern.
- `$select`: Nur bestimmte Felder auswählen.
- `$orderby`: Ergebnisse sortieren.

### 4.1. Curriculum Services

#### Admin Curriculum Service
- **Basis-URL:** `/learning/odatav4/public/admin/curriculum-service/v1`
- **Endpunkte:**
  - `GET /Curricula`: Ruft eine Liste von Curricula ab.
  - `GET /$metadata`: Ruft das Service-Metadatendokument ab.

#### User Curriculum Service
- **Basis-URL:** `/learning/odatav4/public/user/curriculum-service/v1`
- **Endpunkte:**
  - `GET /Curricula`: Ruft eine Liste von Curricula mit benutzerspezifischen Daten ab (z.B. `enrollmentStatus`, `completionStatus`).

### 4.2. Learning Event Services

#### Admin Learning Event Service
- **Basis-URL:** `/learning/odatav4/public/admin/learningevent-service/v1`
- **Endpunkte:**
  - `POST /recordLearningEvents`: Zeichnet ein Lernereignis für einen Benutzer auf.

#### User Learning Event Service
- **Basis-URL:** `/learning/odatav4/public/user/learningevent-service/v1`
- **Endpunkte:**
  - `GET /ExternalLearningEvents`: Ruft extern erfasste Lernereignisse ab.
  - `POST /ExternalLearningEvents`: Erstellt ein neues externes Lernereignis.

### 4.3. Learning Plan Service
- **Basis-URL:** `/learning/odatav4/public/user/learningplan-service/v1`
- **Endpunkte:**
  - `GET /LearningPlans`: Ruft die Lernpläne eines Benutzers ab.

### 4.4. Scheduled Offering Services

#### Admin Scheduled Offering Service
- **Basis-URL:** `/learning/odatav4/public/admin/scheduledoffering-service/v1`
- **Endpunkte:**
  - `GET /ScheduledOfferings`: Ruft geplante Kursangebote ab.

#### User Scheduled Offering Service
- **Basis-URL:** `/learning/odatav4/public/user/scheduledoffering-service/v1`
- **Endpunkte:**
  - `GET /ScheduledOfferings`: Ruft geplante Kursangebote mit benutzerspezifischem Anmeldestatus ab.

### 4.5. Search Services
- **Basis-URL:** `/learning/odatav4/public/admin/search-service/v1`
- **Endpunkte:**
  - `GET /Programs`: Durchsucht Programme.
  - `GET /Students`: Durchsucht Benutzer (Students).
  - `GET /Items`: Durchsucht Lernelemente (Items).

### 4.6. User Assignment Services

#### User Assignment Service v1
- **Basis-URL:** `/learning/odatav4/public/user/userassignment-service/v1`
- **Endpunkte:**
  - `GET /UserPrograms`: Ruft Programmzuweisungen für Benutzer ab.

#### User Assignment Service v2
- **Basis-URL:** `/learning/odatav4/public/user/userassignment-service/v2`
- **Endpunkte:**
  - `POST /itemAssignments`: Weist einem Benutzer ein Lernelement zu.
  - `POST /removeItemAssignments`: Entfernt eine Lernelement-Zuweisung.

### 4.7. User Learning Service
- **Basis-URL:** `/learning/odatav4/public/user/userlearning-service/v1`
- **Endpunkte:**
  - `GET /LearningHistories`: Ruft die Lernhistorie eines Benutzers ab.

### 4.8. User Services

#### Admin User Services
- **v1 Basis-URL:** `/learning/odatav4/public/admin/user-service/v1`
- **v2 Basis-URL:** `/learning/odatav4/public/admin/user-service/v2`
- **Endpunkte (v2):**
  - `POST /MergeUsers`: Führt zwei Benutzerkonten zusammen.
  - `GET /Users`: Ruft Benutzerdaten ab.

#### User Services
- **v1 Basis-URL:** `/learning/odatav4/public/user/user-service/v1`
- **v2 Basis-URL:** `/learning/odatav4/public/user/user-service/v2`
- **Endpunkte:**
  - `GET /Approvals` (v1): Ruft Genehmigungsanfragen ab.
  - `GET /UserAssignments` (v2): Ruft Zuweisungen für den Benutzer ab.

### 4.9. Catalog Services

#### Allgemeine und Benutzer-Katalogsuche
- **Allgemein:** `GET /learning/odatav4/catalogSearch/v1/CatalogItems`
- **Benutzer:** `GET /learning/odatav4/public/user/catalogSearch/v1/CatalogItems`

#### Admin Catalog Service
- **Basis-URL:** `/learning/odatav4/public/admin/catalog-service/v1`
- **Endpunkte:**
  - `GET /CatalogsFeed`: Ruft die Hauptkataloge ab.
  - `GET /CatalogsFeed/{id}/CoursesFeed`: Kurse in einem Katalog.
  - `GET /CatalogsFeed/{id}/CurriculaFeed`: Curricula in einem Katalog.
  - `GET /CatalogsFeed/{id}/ProgramsFeed`: Programme in einem Katalog.
  - `GET /CatalogsFeed/{id}/CollectionsFeed`: Sammlungen in einem Katalog.

### 4.10. Financial Transactions Service
- **Basis-URL:** `/learning/odatav4/public/admin/financialtransactions/v1`
- **Endpunkte:**
  - `GET /FinancialTransactions`: Ruft Finanztransaktionen ab.

---

## 5. Datenmodelle

Hier sind die primären Datenmodelle, die in den API-Antworten verwendet werden.

<details>
<summary>Curriculum</summary>

```json
{
  "curriculumID": "string",
  "title": "string",
  "description": "string",
  "category": "string",
  "difficulty": "string",
  "totalDuration": "number",
  "totalItems": "number",
  "status": "string",
  "createdDate": "datetime",
  "lastModifiedDate": "datetime",
  "language": "string",
  "items": [
    {
      "itemID": "string",
      "title": "string",
      "type": "string",
      "duration": "number",
      "displayOrder": "number"
    }
  ]
}
```
</details>

<details>
<summary>Course</summary>

```json
{
  "courseID": "string",
  "title": "string",
  "description": "string",
  "category": "string",
  "difficulty": "string",
  "duration": "number",
  "language": "string",
  "status": "string",
  "createdDate": "datetime",
  "lastModifiedDate": "datetime",
  "instructorName": "string",
  "format": "string",
  "prerequisites": ["string"],
  "learningObjectives": ["string"]
}
```
</details>

<details>
<summary>Learning Event</summary>

```json
{
  "eventID": "string",
  "studentID": "string",
  "courseID": "string",
  "completionDate": "datetime",
  "completionStatus": "string",
  "score": "number",
  "totalHours": "number",
  "contactHours": "number",
  "instructorName": "string",
  "comments": "string"
}
```
</details>

<details>
<summary>Student</summary>

```json
{
  "studentID": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "status": "string",
  "department": "string",
  "jobTitle": "string",
  "enrollmentDate": "datetime",
  "lastLoginDate": "datetime"
}
```
</details>

<details>
<summary>Scheduled Offering</summary>

```json
{
  "offeringID": "string",
  "courseID": "string",
  "title": "string",
  "startDate": "datetime",
  "endDate": "datetime",
  "location": "string",
  "maxEnrollment": "number",
  "currentEnrollment": "number",
  "status": "string",
  "instructors": [
    {
      "instructorID": "string",
      "firstName": "string",
      "lastName": "string",
      "primary": "boolean"
    }
  ]
}
```
</details>

<details>
<summary>Financial Transaction</summary>

```json
{
  "transactionID": "string",
  "orderNo": "string",
  "studentID": "string",
  "courseID": "string",
  "amount": "decimal",
  "currency": "string",
  "transactionType": "string",
  "transactionDate": "datetime",
  "status": "string",
  "paymentMethod": "string",
  "description": "string",
  "externalTransactionID": "string"
}
```
</details>

---

## 6. Fehlerbehandlung

### HTTP-Statuscodes
- `200 OK`: Erfolgreiche Anfrage.
- `201 Created`: Ressource erfolgreich erstellt.
- `400 Bad Request`: Ungültige Anfrage (z.B. fehlende Parameter).
- `404 Not Found`: Die angeforderte Ressource wurde nicht gefunden.
- `500 Internal Server Error`: Ein interner Serverfehler ist aufgetreten.

### Standard-Fehlerformat
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Eine detaillierte Beschreibung des Fehlers."
  }
}
```

### Häufige Fehlercodes
- `MISSING_PARAM`: Ein erforderlicher Query-Parameter fehlt.
- `MISSING_FIELD`: Ein erforderliches Feld im Request Body fehlt.
- `NOT_FOUND`: Die angeforderte Ressource existiert nicht.
- `INTERNAL_ERROR`: Ein allgemeiner interner Serverfehler.

---

## 7. Workflows & Beispiele

### Workflow: Curriculum-Management

1.  **Alle Curricula abrufen:**
    ```bash
    curl -X GET "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula"
    ```

2.  **Aktive Curricula filtern:**
    ```bash
    curl -X GET "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?$filter=status eq 'Active'"
    ```

3.  **Benutzerspezifische Ansicht abrufen:**
    ```bash
    curl -X GET "http://localhost:5001/learning/odatav4/public/user/curriculum-service/v1/Curricula"
    ```

### Workflow: Learning Event Management

1.  **Lernereignis als Admin aufzeichnen:**
    ```bash
    curl -X POST "http://localhost:5001/learning/odatav4/public/admin/learningevent-service/v1/recordLearningEvents" \
      -H "Content-Type: application/json" \
      -d '{
        "studentID": "USER_001",
        "courseID": "COURSE_001",
        "completionDate": "2024-01-15T17:00:00Z",
        "completionStatus": "Pass",
        "score": 85.5,
        "totalHours": 8.0
      }'
    ```

2.  **Externes Lernereignis als Benutzer erstellen:**
    ```bash
    curl -X POST "http://localhost:5001/learning/odatav4/public/user/learningevent-service/v1/ExternalLearningEvents" \
      -H "Content-Type: application/json" \
      -d '{
        "title": "AWS Certification",
        "provider": "Amazon Web Services",
        "completionDate": "2024-01-20T00:00:00Z",
        "totalHours": 40.0
      }'
    ```

3.  **Lernhistorie des Benutzers abrufen:**
    ```bash
    curl -X GET "http://localhost:5001/learning/odatav4/public/user/userlearning-service/v1/LearningHistories"
    ```

### OData Query-Beispiele

- **Paginierung (Erste 10, dann nächste 10):**
  ```bash
  curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?$top=10"
  curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?$top=10&$skip=10"
  ```

- **Feldauswahl (Nur ID und Titel):**
  ```bash
  curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?$select=curriculumID,title"
  ```

- **Sortierung (Nach Titel aufsteigend):**
  ```bash
  curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?$orderby=title"
  ```

- **Kombinierte Abfrage:**
  ```bash
  # Aktive Curricula, nur ID/Titel/Status, nach Titel sortiert, die ersten 5
  curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?$filter=status eq 'Active'&$select=curriculumID,title,status&$orderby=title&$top=5"
  ```