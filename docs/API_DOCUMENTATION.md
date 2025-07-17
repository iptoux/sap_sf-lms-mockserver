# SAP SuccessFactors LMS MockServer - API Dokumentation

## Inhaltsverzeichnis

1. [Übersicht](#übersicht)
2. [Authentifizierung](#authentifizierung)
3. [REST API Endpunkte](#rest-api-endpunkte)
4. [OData v4 Services](#odata-v4-services)
5. [Datenmodelle](#datenmodelle)
6. [Fehlerbehandlung](#fehlerbehandlung)
7. [Beispiele](#beispiele)

## Übersicht

Diese Dokumentation beschreibt alle verfügbaren API-Endpunkte des SAP SuccessFactors LMS MockServers. Der Server emuliert die vollständige SAP SuccessFactors Learning Management System API mit realistischen Mock-Daten.

**Basis-URL:** `http://localhost:5001`

**Unterstützte Formate:**
- JSON (Standard)
- OData v4 konforme Responses

**CORS:** Aktiviert für alle Origins

## Authentifizierung

Der MockServer erfordert keine Authentifizierung. In einer echten SAP SuccessFactors Umgebung würden OAuth 2.0 oder Basic Authentication verwendet.

## REST API Endpunkte

### 1. System-Endpunkte

#### Health Check
```
GET /health
```

**Beschreibung:** Überprüft den Status des Servers

**Response:**
```json
{
  "status": "healthy",
  "service": "SAP SuccessFactors LMS MockServer"
}
```

#### Root Information
```
GET /
```

**Beschreibung:** Gibt grundlegende Informationen über den Service zurück

**Response:**
```json
{
  "service": "SAP SuccessFactors LMS MockServer",
  "version": "1.0.0",
  "description": "Mock server for SAP SuccessFactors Learning Management System API",
  "endpoints": "See documentation for available endpoints"
}
```

### 2. Partner Extract Configuration

#### Get Partner Extract Configuration
```
GET /learning/public-api/rest/v1/partnerExtractConfig
```

**Parameter:**
- `partnerID` (required): Partner-Identifikator

**Beispiel Request:**
```bash
curl -X GET "http://localhost:5001/learning/public-api/rest/v1/partnerExtractConfig?partnerID=PARTNER001"
```

**Response:**
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
  },
  "errors": null,
  "warnings": null
}
```

#### Update Partner Extract Configuration
```
PUT /learning/public-api/rest/v1/partnerExtractConfig
```

**Request Body:**
```json
{
  "partnerID": "PARTNER001",
  "sftpPath": "/customer/subfolder/path",
  "enabled": true,
  "email": "partner@example.com",
  "extractFrequency": "DAILY"
}
```

### 3. Adhoc Data Extract

#### Create Adhoc Data Extract
```
PUT /learning/public-api/rest/v1/adhocDataExtract
```

**Parameter:**
- `partnerID` (required): Partner-Identifikator

**Request Body:**
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

**Response:**
```json
{
  "restOperationStatusVOX": {
    "operation": "ADHOC_EXTRACT",
    "status": "SUCCESS",
    "data": {
      "REST_RETURN_DATA": null
    }
  },
  "errors": null,
  "warnings": null
}
```

## OData v4 Services

### 1. Curriculum Services

#### Admin Curriculum Service

**Basis-URL:** `/learning/odatav4/public/admin/curriculum-service/v1`

##### Service Metadata
```
GET /learning/odatav4/public/admin/curriculum-service/v1/$metadata
```

**Response:** OData v4 Metadata-Dokument mit EntitySets und EntityTypes

##### Get Curricula
```
GET /learning/odatav4/public/admin/curriculum-service/v1/Curricula
```

**Unterstützte Query-Parameter:**
- `$top`: Anzahl der zurückzugebenden Einträge
- `$skip`: Anzahl der zu überspringenden Einträge
- `$count`: Gesamtanzahl einschließen
- `$filter`: Filterkriterien
- `$select`: Spezifische Felder auswählen
- `$orderby`: Sortierung

**Beispiel:**
```bash
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$top=5&\$count=true"
```

**Response:**
```json
{
  "@odata.context": "$metadata#Curricula",
  "@odata.count": 2,
  "value": [
    {
      "curriculumID": "CURR_001",
      "title": "Management Development Program",
      "description": "Comprehensive management development curriculum for emerging leaders",
      "category": "Leadership",
      "difficulty": "Intermediate",
      "totalDuration": 40.0,
      "totalItems": 5,
      "status": "Active",
      "createdDate": "2023-01-20T10:00:00Z",
      "lastModifiedDate": "2023-12-15T14:00:00Z",
      "language": "English",
      "items": [
        {
          "itemID": "COURSE_001",
          "title": "Leadership Fundamentals",
          "type": "Course",
          "duration": 8.0,
          "displayOrder": 1
        }
      ]
    }
  ]
}
```

#### User Curriculum Service

**Basis-URL:** `/learning/odatav4/public/user/curriculum-service/v1`

##### Get User Curricula
```
GET /learning/odatav4/public/user/curriculum-service/v1/Curricula
```

**Response:** Ähnlich wie Admin-Service, aber mit benutzerspezifischen Feldern:
- `enrollmentStatus`: Anmeldestatus des Benutzers
- `completionStatus`: Abschlussstatus
- `progressPercentage`: Fortschritt in Prozent
- `enrollmentDate`: Anmeldedatum

### 2. Learning Event Services

#### Admin Learning Event Service

**Basis-URL:** `/learning/odatav4/public/admin/learningevent-service/v1`

##### Record Learning Event
```
POST /learning/odatav4/public/admin/learningevent-service/v1/recordLearningEvents
```

**Request Body:**
```json
{
  "studentID": "USER_001",
  "courseID": "COURSE_001",
  "completionDate": "2024-01-15T17:00:00Z",
  "completionStatus": "Pass",
  "score": 85.5,
  "totalHours": 8.0,
  "contactHours": 8.0,
  "instructorName": "Dr. Sarah Johnson",
  "comments": "Excellent performance"
}
```

**Response:**
```json
{
  "eventID": "EVENT_USER_001_20240115170000",
  "studentID": "USER_001",
  "courseID": "COURSE_001",
  "completionDate": "2024-01-15T17:00:00Z",
  "completionStatus": "Pass",
  "score": 85.5,
  "totalHours": 8.0,
  "contactHours": 8.0,
  "instructorName": "Dr. Sarah Johnson",
  "comments": "Excellent performance",
  "recordedBy": "ADMIN_001",
  "recordedDate": "2024-01-15T17:05:00Z"
}
```

#### User Learning Event Service

**Basis-URL:** `/learning/odatav4/public/user/learningevent-service/v1`

##### Get External Learning Events
```
GET /learning/odatav4/public/user/learningevent-service/v1/ExternalLearningEvents
```

**Response:**
```json
{
  "@odata.context": "$metadata#ExternalLearningEvents",
  "value": [
    {
      "eventID": "EXT_EVENT_001",
      "title": "AWS Cloud Practitioner Certification",
      "provider": "Amazon Web Services",
      "completionDate": "2024-01-10T00:00:00Z",
      "certificateNumber": "AWS-CP-2024-001",
      "totalHours": 40.0,
      "description": "Cloud computing fundamentals certification"
    }
  ]
}
```

##### Create External Learning Event
```
POST /learning/odatav4/public/user/learningevent-service/v1/ExternalLearningEvents
```

**Request Body:**
```json
{
  "title": "Project Management Professional (PMP)",
  "provider": "Project Management Institute",
  "completionDate": "2024-01-20T00:00:00Z",
  "certificateNumber": "PMP-2024-12345",
  "totalHours": 35.0,
  "description": "Professional project management certification"
}
```

### 3. Learning Plan Service

**Basis-URL:** `/learning/odatav4/public/user/learningplan-service/v1`

#### Get Learning Plans
```
GET /learning/odatav4/public/user/learningplan-service/v1/LearningPlans
```

**Response:**
```json
{
  "@odata.context": "$metadata#LearningPlans",
  "value": [
    {
      "planID": "PLAN_001",
      "studentID": "USER_001",
      "courseID": "COURSE_001",
      "assignmentDate": "2024-01-01T09:00:00Z",
      "dueDate": "2024-03-01T17:00:00Z",
      "completionStatus": "In Progress",
      "contactHours": 8.0,
      "totalHours": 8.0,
      "instructorName": "Dr. Sarah Johnson",
      "comments": "Excellent progress so far"
    }
  ]
}
```

### 4. Scheduled Offering Services

#### Admin Scheduled Offering Service

**Basis-URL:** `/learning/odatav4/public/admin/scheduledoffering-service/v1`

##### Get Scheduled Offerings
```
GET /learning/odatav4/public/admin/scheduledoffering-service/v1/ScheduledOfferings
```

**Response:**
```json
{
  "@odata.context": "$metadata#ScheduledOfferings",
  "value": [
    {
      "offeringID": "OFFER_001",
      "courseID": "COURSE_001",
      "title": "Leadership Fundamentals - January 2024",
      "startDate": "2024-01-15T09:00:00Z",
      "endDate": "2024-01-17T17:00:00Z",
      "location": "Conference Room A",
      "maxEnrollment": 20,
      "currentEnrollment": 15,
      "status": "Scheduled",
      "instructors": [
        {
          "instructorID": "INST_001",
          "firstName": "Sarah",
          "lastName": "Johnson",
          "primary": true
        }
      ]
    }
  ]
}
```

#### User Scheduled Offering Service

**Basis-URL:** `/learning/odatav4/public/user/scheduledoffering-service/v1`

##### Get User Scheduled Offerings
```
GET /learning/odatav4/public/user/scheduledoffering-service/v1/ScheduledOfferings
```

**Response:** Ähnlich wie Admin-Service, aber mit benutzerspezifischen Feldern:
- `enrollmentStatus`: Anmeldestatus des Benutzers
- `attendanceStatus`: Teilnahmestatus

### 5. Search Services

#### Admin Search Service

**Basis-URL:** `/learning/odatav4/public/admin/search-service/v1`

##### Search Programs
```
GET /learning/odatav4/public/admin/search-service/v1/Programs
```

##### Search Students
```
GET /learning/odatav4/public/admin/search-service/v1/Students
```

**Response:**
```json
{
  "@odata.context": "$metadata#Students",
  "value": [
    {
      "studentID": "USER_001",
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@company.com",
      "status": "Active",
      "department": "Engineering",
      "jobTitle": "Software Developer",
      "enrollmentDate": "2023-01-15T09:00:00Z",
      "lastLoginDate": "2024-01-14T14:30:00Z"
    }
  ]
}
```

##### Search Items
```
GET /learning/odatav4/public/admin/search-service/v1/Items
```

### 6. User Assignment Services

#### User Assignment Service v1

**Basis-URL:** `/learning/odatav4/public/user/userassignment-service/v1`

##### Get User Program Assignments
```
GET /learning/odatav4/public/user/userassignment-service/v1/UserPrograms
```

#### User Assignment Service v2

**Basis-URL:** `/learning/odatav4/public/user/userassignment-service/v2`

##### Create Item Assignment
```
POST /learning/odatav4/public/user/userassignment-service/v2/itemAssignments
```

**Request Body:**
```json
{
  "studentID": "USER_001",
  "itemID": "COURSE_001",
  "dueDate": "2024-03-01T17:00:00Z",
  "assignedBy": "SUPERVISOR_001",
  "priority": "High"
}
```

**Response:**
```json
{
  "assignmentID": "ASSIGN_20240115170500",
  "studentID": "USER_001",
  "itemID": "COURSE_001",
  "assignmentDate": "2024-01-15T17:05:00Z",
  "dueDate": "2024-03-01T17:00:00Z",
  "assignedBy": "SUPERVISOR_001",
  "priority": "High",
  "status": "Active"
}
```

##### Remove Item Assignment
```
POST /learning/odatav4/public/user/userassignment-service/v2/removeItemAssignments
```

**Request Body:**
```json
{
  "assignmentID": "ASSIGN_001",
  "removalReason": "Course no longer required"
}
```

### 7. User Learning Service

**Basis-URL:** `/learning/odatav4/public/user/userlearning-service/v1`

#### Get Learning Histories
```
GET /learning/odatav4/public/user/userlearning-service/v1/LearningHistories
```

**Response:**
```json
{
  "@odata.context": "$metadata#LearningHistories",
  "value": [
    {
      "historyID": "HIST_001",
      "studentID": "USER_001",
      "courseID": "COURSE_001",
      "completionDate": "2023-12-15T17:00:00Z",
      "completionStatus": "Pass",
      "score": 85.5,
      "totalHours": 8.0
    }
  ]
}
```

### 8. User Services

#### Admin User Service v1

**Basis-URL:** `/learning/odatav4/public/admin/user-service/v1`

#### Admin User Service v2

**Basis-URL:** `/learning/odatav4/public/admin/user-service/v2`

##### Merge Users
```
POST /learning/odatav4/public/admin/user-service/v2/MergeUsers
```

**Request Body:**
```json
{
  "fromUserID": "USER_OLD",
  "toUserID": "USER_NEW",
  "fromPersonGUID": "GUID_OLD",
  "toPersonGUID": "GUID_NEW"
}
```

##### Get Users
```
GET /learning/odatav4/public/admin/user-service/v2/Users
```

#### User Service v1

**Basis-URL:** `/learning/odatav4/public/user/user-service/v1`

##### Get Approvals
```
GET /learning/odatav4/public/user/user-service/v1/Approvals
```

#### User Service v2

**Basis-URL:** `/learning/odatav4/public/user/user-service/v2`

##### Get User Assignments
```
GET /learning/odatav4/public/user/user-service/v2/UserAssignments
```

### 9. Catalog Services

#### Catalog Search v1

**Basis-URL:** `/learning/odatav4/catalogSearch/v1`

##### Search Catalog Items
```
GET /learning/odatav4/catalogSearch/v1/CatalogItems
```

#### User Catalog Search v1

**Basis-URL:** `/learning/odatav4/public/user/catalogSearch/v1`

##### Search Catalog Items (User)
```
GET /learning/odatav4/public/user/catalogSearch/v1/CatalogItems
```

#### Admin Catalog Service v1

**Basis-URL:** `/learning/odatav4/public/admin/catalog-service/v1`

##### Get Catalogs
```
GET /learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed
```

##### Get Catalog Courses
```
GET /learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/{catalogId}/CoursesFeed
```

##### Get Catalog Curricula
```
GET /learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/{catalogId}/CurriculaFeed
```

##### Get Catalog Programs
```
GET /learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/{catalogId}/ProgramsFeed
```

##### Get Catalog Collections
```
GET /learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/{catalogId}/CollectionsFeed
```

### 10. Financial Transactions Service

**Basis-URL:** `/learning/odatav4/public/admin/financialtransactions/v1`

#### Get Financial Transactions
```
GET /learning/odatav4/public/admin/financialtransactions/v1/FinancialTransactions
```

**Response:**
```json
{
  "@odata.context": "$metadata#FinancialTransactions",
  "value": [
    {
      "transactionID": "TXN_001",
      "orderNo": "ORD_2024_001",
      "studentID": "USER_001",
      "courseID": "COURSE_001",
      "amount": 299.99,
      "currency": "USD",
      "transactionType": "Purchase",
      "transactionDate": "2024-01-15T10:30:00Z",
      "status": "Completed",
      "paymentMethod": "Credit Card",
      "description": "Leadership Fundamentals Course Purchase",
      "externalTransactionID": "EXT_TXN_12345"
    }
  ]
}
```

## Datenmodelle

### Curriculum
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

### Course
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

### Learning Event
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

### Student
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

### Scheduled Offering
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

### Financial Transaction
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

## Fehlerbehandlung

### Standard-Fehlerformat
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Detailed error message"
  }
}
```

### HTTP-Statuscodes
- `200 OK`: Erfolgreiche Anfrage
- `201 Created`: Ressource erfolgreich erstellt
- `400 Bad Request`: Ungültige Anfrage
- `404 Not Found`: Ressource nicht gefunden
- `500 Internal Server Error`: Serverfehler

### Häufige Fehlercodes
- `MISSING_PARAM`: Erforderlicher Parameter fehlt
- `MISSING_FIELD`: Erforderliches Feld im Request Body fehlt
- `NOT_FOUND`: Angeforderte Ressource nicht gefunden
- `INTERNAL_ERROR`: Interner Serverfehler

## Beispiele

### Vollständiger Workflow: Curriculum-Management

#### 1. Curricula abrufen
```bash
curl -X GET "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula"
```

#### 2. Spezifisches Curriculum mit Filterung
```bash
curl -X GET "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$filter=status eq 'Active'"
```

#### 3. Benutzer-spezifische Curriculum-Ansicht
```bash
curl -X GET "http://localhost:5001/learning/odatav4/public/user/curriculum-service/v1/Curricula"
```

### Vollständiger Workflow: Learning Event Management

#### 1. Lernereignis aufzeichnen (Admin)
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

#### 2. Externes Lernereignis erstellen (Benutzer)
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

#### 3. Lernhistorie abrufen
```bash
curl -X GET "http://localhost:5001/learning/odatav4/public/user/userlearning-service/v1/LearningHistories"
```

### OData Query-Beispiele

#### Paginierung
```bash
# Erste 10 Einträge
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$top=10"

# Nächste 10 Einträge (11-20)
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$top=10&\$skip=10"
```

#### Filterung
```bash
# Aktive Curricula
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$filter=status eq 'Active'"

# Curricula mit mehr als 5 Items
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$filter=totalItems gt 5"
```

#### Feldauswahl
```bash
# Nur ID und Titel
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$select=curriculumID,title"
```

#### Sortierung
```bash
# Nach Titel sortiert
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$orderby=title"

# Nach Erstellungsdatum absteigend
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$orderby=createdDate desc"
```

#### Kombinierte Queries
```bash
# Aktive Curricula, nur Titel und Status, sortiert nach Titel, erste 5
curl "http://localhost:5001/learning/odatav4/public/admin/curriculum-service/v1/Curricula?\$filter=status eq 'Active'&\$select=curriculumID,title,status&\$orderby=title&\$top=5"
```

---

**Entwickelt von:** Manus AI  
**Letzte Aktualisierung:** Januar 2024  
**Version:** 1.0.0

