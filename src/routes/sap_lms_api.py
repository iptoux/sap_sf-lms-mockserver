from flask import Blueprint, jsonify, request
from flask_cors import CORS
import json
import os

sap_lms_bp = Blueprint('sap_lms', __name__)

# Enable CORS for all routes in this blueprint
CORS(sap_lms_bp)

# Helper function to load mock data
def load_mock_data(filename):
    """Load mock data from JSON file"""
    mock_data_path = os.path.join(os.path.dirname(__file__), '..', 'mock_data', filename)
    try:
        with open(mock_data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": f"Mock data file {filename} not found"}
    except json.JSONDecodeError:
        return {"error": f"Invalid JSON in {filename}"}

# Helper function to create standard response format
def create_response(data, status="SUCCESS", errors=None, warnings=None):
    """Create standardized response format for SAP LMS API"""
    return {
        "restOperationStatusVOX": {
            "operation": None,
            "status": status,
            "data": data
        },
        "errors": errors,
        "warnings": warnings
    }

# 2.1 /learning/public-api/rest/v1/partnerExtractConfig
@sap_lms_bp.route('/learning/public-api/rest/v1/partnerExtractConfig', methods=['GET'])
def get_partner_extract_config():
    partner_id = request.args.get('partnerID')
    if not partner_id:
        return jsonify(create_response(None, "FAILED", [{"code": "MISSING_PARAM", "message": "partnerID parameter is required"}])), 400
    
    mock_data = load_mock_data('partner_extract_config.json')
    return jsonify(create_response(mock_data))

@sap_lms_bp.route('/learning/public-api/rest/v1/partnerExtractConfig', methods=['PUT'])
def update_partner_extract_config():
    data = request.json
    mock_data = load_mock_data('partner_extract_config.json')
    return jsonify(create_response(mock_data))

# 2.2 /learning/public-api/rest/v1/adhocDataExtract
@sap_lms_bp.route('/learning/public-api/rest/v1/adhocDataExtract', methods=['PUT'])
def adhoc_data_extract():
    partner_id = request.args.get('partnerID')
    if not partner_id:
        return jsonify(create_response(None, "FAILED", [{"code": "MISSING_PARAM", "message": "partnerID parameter is required"}])), 400
    
    return jsonify(create_response({"REST_RETURN_DATA": None}))

# 2.3 admin/curriculum-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/admin/curriculum-service/v1/$metadata', methods=['GET'])
def admin_curriculum_service_metadata():
    mock_data = load_mock_data('admin_curriculum_service_metadata.json')
    return jsonify(mock_data)

# 2.4 user/curriculum-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/curriculum-service/v1/$metadata', methods=['GET'])
def user_curriculum_service_metadata():
    mock_data = load_mock_data('user_curriculum_service_metadata.json')
    return jsonify(mock_data)

# 2.5 admin/learningevent-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/admin/learningevent-service/v1/$metadata', methods=['GET'])
def admin_learningevent_service_metadata():
    mock_data = load_mock_data('admin_learningevent_service_metadata.json')
    return jsonify(mock_data)

# 2.6 user/learningevent-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/learningevent-service/v1/$metadata', methods=['GET'])
def user_learningevent_service_metadata():
    mock_data = load_mock_data('user_learningevent_service_metadata.json')
    return jsonify(mock_data)

# 2.7 user/learningplan-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/learningplan-service/v1/$metadata', methods=['GET'])
def user_learningplan_service_metadata():
    mock_data = load_mock_data('user_learningplan_service_metadata.json')
    return jsonify(mock_data)

# 2.8 admin/scheduledoffering-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/admin/scheduledoffering-service/v1/$metadata', methods=['GET'])
def admin_scheduledoffering_service_metadata():
    mock_data = load_mock_data('admin_scheduledoffering_service_metadata.json')
    return jsonify(mock_data)

# 2.9 user/scheduledoffering-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/scheduledoffering-service/v1/$metadata', methods=['GET'])
def user_scheduledoffering_service_metadata():
    mock_data = load_mock_data('user_scheduledoffering_service_metadata.json')
    return jsonify(mock_data)

# 2.10 admin/search-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/admin/search-service/v1/$metadata', methods=['GET'])
def admin_search_service_metadata():
    mock_data = load_mock_data('admin_search_service_metadata.json')
    return jsonify(mock_data)

# 2.11 user/userassignment-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/userassignment-service/v1/$metadata', methods=['GET'])
def user_userassignment_service_v1_metadata():
    mock_data = load_mock_data('user_userassignment_service_v1_metadata.json')
    return jsonify(mock_data)

# 2.12 user/userassignment-service/v2 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/userassignment-service/v2/$metadata', methods=['GET'])
def user_userassignment_service_v2_metadata():
    mock_data = load_mock_data('user_userassignment_service_v2_metadata.json')
    return jsonify(mock_data)

# 2.13 user/userlearning-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/userlearning-service/v1/$metadata', methods=['GET'])
def user_userlearning_service_metadata():
    mock_data = load_mock_data('user_userlearning_service_metadata.json')
    return jsonify(mock_data)

# 2.14 admin/user-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/admin/user-service/v1/$metadata', methods=['GET'])
def admin_user_service_v1_metadata():
    mock_data = load_mock_data('admin_user_service_v1_metadata.json')
    return jsonify(mock_data)

# 2.15 admin/user-service/v2 Metadata
@sap_lms_bp.route('/learning/odatav4/public/admin/user-service/v2/$metadata', methods=['GET'])
def admin_user_service_v2_metadata():
    mock_data = load_mock_data('admin_user_service_v2_metadata.json')
    return jsonify(mock_data)

# 2.16 user/user-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/user-service/v1/$metadata', methods=['GET'])
def user_user_service_v1_metadata():
    mock_data = load_mock_data('user_user_service_v1_metadata.json')
    return jsonify(mock_data)

# 2.17 user/user-service/v2 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/user-service/v2/$metadata', methods=['POST'])
def user_user_service_v2_metadata():
    mock_data = load_mock_data('user_user_service_v2_metadata.json')
    return jsonify(mock_data)

# 2.18 catalogSearch/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/catalogSearch/v1/$metadata', methods=['GET'])
def catalog_search_v1_metadata():
    mock_data = load_mock_data('catalog_search_v1_metadata.json')
    return jsonify(mock_data)

# 2.19 user/catalogSearch/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/catalogSearch/v1/$metadata', methods=['GET'])
def user_catalog_search_v1_metadata():
    mock_data = load_mock_data('user_catalog_search_v1_metadata.json')
    return jsonify(mock_data)

# 2.20 admin/learningEvent/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/admin/learningEvent/v1/$metadata', methods=['GET'])
def admin_learning_event_v1_metadata():
    mock_data = load_mock_data('admin_learning_event_v1_metadata.json')
    return jsonify(mock_data)

# 2.21 user/learningEvent/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/learningEvent/v1/$metadata', methods=['GET'])
def user_learning_event_v1_metadata():
    mock_data = load_mock_data('user_learning_event_v1_metadata.json')
    return jsonify(mock_data)

# 2.22 user/itemAssignment/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/itemAssignment/v1/$metadata', methods=['GET'])
def user_item_assignment_v1_metadata():
    mock_data = load_mock_data('user_item_assignment_v1_metadata.json')
    return jsonify(mock_data)

# 2.23 admin/userService/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/admin/userService/v1/$metadata', methods=['GET'])
def admin_user_service_v1_metadata_alt():
    mock_data = load_mock_data('admin_user_service_v1_metadata_alt.json')
    return jsonify(mock_data)

# 2.24 user/learningPlan/v1 Metadata Call
@sap_lms_bp.route('/learning/odatav4/user/learningPlan/v1/$metadata', methods=['GET'])
def user_learning_plan_v1_metadata():
    mock_data = load_mock_data('user_learning_plan_v1_metadata.json')
    return jsonify(mock_data)

# 2.25 user/learningHistory/v1 Metadata Call
@sap_lms_bp.route('/learning/odatav4/public/user/learningHistory/v1/$metadata', methods=['GET'])
def user_learning_history_v1_metadata():
    mock_data = load_mock_data('user_learning_history_v1_metadata.json')
    return jsonify(mock_data)

# 2.26 admin/searchStudent/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/searchStudent/v1/$metadata', methods=['GET'])
def admin_search_student_v1_metadata():
    mock_data = load_mock_data('admin_search_student_v1_metadata.json')
    return jsonify(mock_data)

# 2.27 searchStudent/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/searchStudent/v1/$metadata', methods=['GET'])
def search_student_v1_metadata():
    mock_data = load_mock_data('search_student_v1_metadata.json')
    return jsonify(mock_data)

# 2.28 user/v1 Metadata Call
@sap_lms_bp.route('/learning/odatav4/user/v1/$metadata', methods=['GET'])
def user_v1_metadata():
    mock_data = load_mock_data('user_v1_metadata.json')
    return jsonify(mock_data)

# 2.29 curriculum/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/curriculum/v1/$metadata', methods=['GET'])
def curriculum_v1_metadata():
    mock_data = load_mock_data('curriculum_v1_metadata.json')
    return jsonify(mock_data)

# 2.30 user/curriculum/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/user/curriculum/v1/$metadata', methods=['GET'])
def user_curriculum_v1_metadata():
    mock_data = load_mock_data('user_curriculum_v1_metadata.json')
    return jsonify(mock_data)

# 2.31 admin/searchItem/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/admin/searchItem/v1/$metadata', methods=['GET'])
def admin_search_item_v1_metadata():
    mock_data = load_mock_data('admin_search_item_v1_metadata.json')
    return jsonify(mock_data)

# 2.32 admin/searchCurriculum/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/admin/searchCurriculum/v1/$metadata', methods=['GET'])
def admin_search_curriculum_v1_metadata():
    mock_data = load_mock_data('admin_search_curriculum_v1_metadata.json')
    return jsonify(mock_data)

# 2.33 searchCurriculum/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/searchCurriculum/v1/$metadata', methods=['GET'])
def search_curriculum_v1_metadata():
    mock_data = load_mock_data('search_curriculum_v1_metadata.json')
    return jsonify(mock_data)

# 2.34 user/learningEvent/v1 Metadata (duplicate endpoint with different path)
@sap_lms_bp.route('/learning/odatav4/public/user/learningEvent/v1/$metadata', methods=['GET'])
def user_learning_event_v1_metadata_alt():
    mock_data = load_mock_data('user_learning_event_v1_metadata_alt.json')
    return jsonify(mock_data)

# 2.35 admin/catalog-service/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/admin/catalog-service/v1/$metadata', methods=['GET'])
def admin_catalog_service_v1_metadata():
    mock_data = load_mock_data('admin_catalog_service_v1_metadata.json')
    return jsonify(mock_data)

# Catalog service endpoints
@sap_lms_bp.route('/learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed', methods=['GET'])
def catalog_details():
    mock_data = load_mock_data('catalog_details.json')
    return jsonify(mock_data)

@sap_lms_bp.route('/learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/<catalog_id>/CoursesFeed', methods=['GET'])
def catalog_courses(catalog_id):
    mock_data = load_mock_data('catalog_courses.json')
    return jsonify(mock_data)

@sap_lms_bp.route('/learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/<catalog_id>/CurriculaFeed', methods=['GET'])
def catalog_curricula(catalog_id):
    mock_data = load_mock_data('catalog_curricula.json')
    return jsonify(mock_data)

@sap_lms_bp.route('/learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/<catalog_id>/ProgramsFeed', methods=['GET'])
def catalog_programs(catalog_id):
    mock_data = load_mock_data('catalog_programs.json')
    return jsonify(mock_data)

@sap_lms_bp.route('/learning/odatav4/public/admin/catalog-service/v1/CatalogsFeed/<catalog_id>/CollectionsFeed', methods=['GET'])
def catalog_collections(catalog_id):
    mock_data = load_mock_data('catalog_collections.json')
    return jsonify(mock_data)

# 2.36 admin/financialtransactions/v1 Metadata
@sap_lms_bp.route('/learning/odatav4/public/admin/financialtransactions/v1/$metadata', methods=['GET'])
def admin_financial_transactions_v1_metadata():
    mock_data = load_mock_data('admin_financial_transactions_v1_metadata.json')
    return jsonify(mock_data)

# Health check endpoint
@sap_lms_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "SAP SuccessFactors LMS MockServer"})

# Root endpoint
@sap_lms_bp.route('/', methods=['GET'])
def root():
    return jsonify({
        "service": "SAP SuccessFactors LMS MockServer",
        "version": "1.0.0",
        "description": "Mock server for SAP SuccessFactors Learning Management System API",
        "endpoints": "See documentation for available endpoints"
    })


# Additional functional endpoints for data operations

# OData helper functions
def create_odata_response(data, context="$metadata", count=None):
    """Create OData v4 compliant response"""
    response = {
        "@odata.context": context
    }
    if count is not None:
        response["@odata.count"] = count
    
    if isinstance(data, list):
        response["value"] = data
    else:
        response.update(data)
    
    return response

def parse_odata_query(request):
    """Parse OData query parameters"""
    return {
        'filter': request.args.get('$filter'),
        'select': request.args.get('$select'),
        'expand': request.args.get('$expand'),
        'orderby': request.args.get('$orderby'),
        'top': request.args.get('$top', type=int),
        'skip': request.args.get('$skip', type=int),
        'count': request.args.get('$count', 'false').lower() == 'true'
    }

# Curriculum Service Data Endpoints
@sap_lms_bp.route('/learning/odatav4/public/admin/curriculum-service/v1/Curricula', methods=['GET'])
def admin_get_curricula():
    """Get curricula for admin operations"""
    query_params = parse_odata_query(request)
    mock_data = load_mock_data('catalog_curricula.json')
    curricula = mock_data.get('value', [])
    
    # Apply basic filtering if needed
    if query_params['top']:
        curricula = curricula[:query_params['top']]
    
    return jsonify(create_odata_response(
        curricula, 
        "$metadata#Curricula",
        len(curricula) if query_params['count'] else None
    ))

@sap_lms_bp.route('/learning/odatav4/public/user/curriculum-service/v1/Curricula', methods=['GET'])
def user_get_curricula():
    """Get curricula for user operations"""
    query_params = parse_odata_query(request)
    mock_data = load_mock_data('catalog_curricula.json')
    curricula = mock_data.get('value', [])
    
    # Add user-specific enrollment information
    for curriculum in curricula:
        curriculum['enrollmentStatus'] = 'Enrolled'
        curriculum['completionStatus'] = 'In Progress'
        curriculum['progressPercentage'] = 65.5
        curriculum['enrollmentDate'] = '2024-01-01T09:00:00Z'
    
    if query_params['top']:
        curricula = curricula[:query_params['top']]
    
    return jsonify(create_odata_response(
        curricula,
        "$metadata#Curricula",
        len(curricula) if query_params['count'] else None
    ))

# Learning Event Service Data Endpoints
@sap_lms_bp.route('/learning/odatav4/public/admin/learningevent-service/v1/recordLearningEvents', methods=['POST'])
def admin_record_learning_event():
    """Record a learning event (admin)"""
    event_data = request.get_json()
    
    # Validate required fields
    required_fields = ['studentID', 'courseID', 'completionDate', 'completionStatus']
    for field in required_fields:
        if field not in event_data:
            return jsonify({
                "error": {
                    "code": "MISSING_FIELD",
                    "message": f"Required field '{field}' is missing"
                }
            }), 400
    
    # Create response
    response_data = {
        "eventID": f"EVENT_{len(str(event_data.get('studentID', '')))}_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "studentID": event_data['studentID'],
        "courseID": event_data['courseID'],
        "completionDate": event_data['completionDate'],
        "completionStatus": event_data['completionStatus'],
        "score": event_data.get('score', 0.0),
        "totalHours": event_data.get('totalHours', 0.0),
        "contactHours": event_data.get('contactHours', 0.0),
        "instructorName": event_data.get('instructorName', ''),
        "comments": event_data.get('comments', ''),
        "recordedBy": "ADMIN_001",
        "recordedDate": datetime.utcnow().isoformat() + "Z"
    }
    
    return jsonify(response_data), 201

@sap_lms_bp.route('/learning/odatav4/public/user/learningevent-service/v1/ExternalLearningEvents', methods=['GET'])
def user_get_external_learning_events():
    """Get external learning events for user"""
    query_params = parse_odata_query(request)
    
    mock_events = [
        {
            "eventID": "EXT_EVENT_001",
            "title": "AWS Cloud Practitioner Certification",
            "provider": "Amazon Web Services",
            "completionDate": "2024-01-10T00:00:00Z",
            "certificateNumber": "AWS-CP-2024-001",
            "totalHours": 40.0,
            "description": "Cloud computing fundamentals certification"
        },
        {
            "eventID": "EXT_EVENT_002",
            "title": "Project Management Professional (PMP)",
            "provider": "Project Management Institute",
            "completionDate": "2023-12-15T00:00:00Z",
            "certificateNumber": "PMP-2023-12345",
            "totalHours": 35.0,
            "description": "Professional project management certification"
        },
        {
            "eventID": "EXT_EVENT_003",
            "title": "Certified Scrum Master",
            "provider": "Scrum Alliance",
            "completionDate": "2023-11-20T00:00:00Z",
            "certificateNumber": "CSM-2023-67890",
            "totalHours": 16.0,
            "description": "Agile project management certification"
        }
    ]
    
    if query_params['top']:
        mock_events = mock_events[:query_params['top']]
    
    return jsonify(create_odata_response(
        mock_events,
        "$metadata#ExternalLearningEvents",
        len(mock_events) if query_params['count'] else None
    ))

@sap_lms_bp.route('/learning/odatav4/public/user/learningevent-service/v1/ExternalLearningEvents', methods=['POST'])
def user_create_external_learning_event():
    """Create external learning event for user"""
    event_data = request.get_json()
    
    # Validate required fields
    required_fields = ['title', 'provider', 'completionDate']
    for field in required_fields:
        if field not in event_data:
            return jsonify({
                "error": {
                    "code": "MISSING_FIELD",
                    "message": f"Required field '{field}' is missing"
                }
            }), 400
    
    # Create response
    response_data = {
        "eventID": f"EXT_EVENT_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "title": event_data['title'],
        "provider": event_data['provider'],
        "completionDate": event_data['completionDate'],
        "certificateNumber": event_data.get('certificateNumber', ''),
        "totalHours": event_data.get('totalHours', 0.0),
        "description": event_data.get('description', ''),
        "createdDate": datetime.utcnow().isoformat() + "Z"
    }
    
    return jsonify(response_data), 201

# Learning Plan Service Data Endpoints
@sap_lms_bp.route('/learning/odatav4/public/user/learningplan-service/v1/LearningPlans', methods=['GET'])
def user_get_learning_plans():
    """Get learning plans for user"""
    query_params = parse_odata_query(request)
    
    mock_plans = [
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
        },
        {
            "planID": "PLAN_002",
            "studentID": "USER_001",
            "courseID": "COURSE_002",
            "assignmentDate": "2024-01-15T09:00:00Z",
            "dueDate": "2024-04-15T17:00:00Z",
            "completionStatus": "Not Started",
            "contactHours": 16.0,
            "totalHours": 16.0,
            "instructorName": "Prof. Michael Chen",
            "comments": "Prerequisites completed"
        },
        {
            "planID": "PLAN_003",
            "studentID": "USER_001",
            "courseID": "COURSE_003",
            "assignmentDate": "2023-12-01T09:00:00Z",
            "dueDate": "2024-01-31T17:00:00Z",
            "completionStatus": "Completed",
            "contactHours": 2.0,
            "totalHours": 2.0,
            "instructorName": "Security Team",
            "comments": "Mandatory compliance training completed"
        }
    ]
    
    if query_params['top']:
        mock_plans = mock_plans[:query_params['top']]
    
    return jsonify(create_odata_response(
        mock_plans,
        "$metadata#LearningPlans",
        len(mock_plans) if query_params['count'] else None
    ))

# Scheduled Offering Service Data Endpoints
@sap_lms_bp.route('/learning/odatav4/public/admin/scheduledoffering-service/v1/ScheduledOfferings', methods=['GET'])
def admin_get_scheduled_offerings():
    """Get scheduled offerings for admin operations"""
    query_params = parse_odata_query(request)
    
    mock_offerings = [
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
                    "primary": True
                }
            ]
        },
        {
            "offeringID": "OFFER_002",
            "courseID": "COURSE_002",
            "title": "Data Analysis with Python - February 2024",
            "startDate": "2024-02-01T09:00:00Z",
            "endDate": "2024-02-05T17:00:00Z",
            "location": "Virtual Classroom",
            "maxEnrollment": 30,
            "currentEnrollment": 25,
            "status": "In Progress",
            "instructors": [
                {
                    "instructorID": "INST_002",
                    "firstName": "Michael",
                    "lastName": "Chen",
                    "primary": True
                }
            ]
        },
        {
            "offeringID": "OFFER_003",
            "courseID": "COURSE_003",
            "title": "Information Security Awareness - March 2024",
            "startDate": "2024-03-01T14:00:00Z",
            "endDate": "2024-03-01T16:00:00Z",
            "location": "Online",
            "maxEnrollment": 100,
            "currentEnrollment": 45,
            "status": "Scheduled",
            "instructors": [
                {
                    "instructorID": "INST_003",
                    "firstName": "Security",
                    "lastName": "Team",
                    "primary": True
                }
            ]
        }
    ]
    
    if query_params['top']:
        mock_offerings = mock_offerings[:query_params['top']]
    
    return jsonify(create_odata_response(
        mock_offerings,
        "$metadata#ScheduledOfferings",
        len(mock_offerings) if query_params['count'] else None
    ))

@sap_lms_bp.route('/learning/odatav4/public/user/scheduledoffering-service/v1/ScheduledOfferings', methods=['GET'])
def user_get_scheduled_offerings():
    """Get scheduled offerings for user operations"""
    query_params = parse_odata_query(request)
    
    mock_offerings = [
        {
            "offeringID": "OFFER_001",
            "courseID": "COURSE_001",
            "title": "Leadership Fundamentals - January 2024",
            "startDate": "2024-01-15T09:00:00Z",
            "endDate": "2024-01-17T17:00:00Z",
            "location": "Conference Room A",
            "enrollmentStatus": "Enrolled",
            "attendanceStatus": "Confirmed"
        },
        {
            "offeringID": "OFFER_003",
            "courseID": "COURSE_003",
            "title": "Information Security Awareness - March 2024",
            "startDate": "2024-03-01T14:00:00Z",
            "endDate": "2024-03-01T16:00:00Z",
            "location": "Online",
            "enrollmentStatus": "Available",
            "attendanceStatus": "Not Enrolled"
        },
        {
            "offeringID": "OFFER_004",
            "courseID": "COURSE_004",
            "title": "Strategic Thinking Workshop - April 2024",
            "startDate": "2024-04-10T09:00:00Z",
            "endDate": "2024-04-12T17:00:00Z",
            "location": "Training Center",
            "enrollmentStatus": "Waitlisted",
            "attendanceStatus": "Pending"
        }
    ]
    
    if query_params['top']:
        mock_offerings = mock_offerings[:query_params['top']]
    
    return jsonify(create_odata_response(
        mock_offerings,
        "$metadata#ScheduledOfferings",
        len(mock_offerings) if query_params['count'] else None
    ))

# Search Service Data Endpoints
@sap_lms_bp.route('/learning/odatav4/public/admin/search-service/v1/Programs', methods=['GET'])
def admin_search_programs():
    """Search programs (admin)"""
    query_params = parse_odata_query(request)
    mock_data = load_mock_data('catalog_programs.json')
    programs = mock_data.get('value', [])
    
    if query_params['top']:
        programs = programs[:query_params['top']]
    
    return jsonify(create_odata_response(
        programs,
        "$metadata#Programs",
        len(programs) if query_params['count'] else None
    ))

@sap_lms_bp.route('/learning/odatav4/public/admin/search-service/v1/Students', methods=['GET'])
def admin_search_students():
    """Search students (admin)"""
    query_params = parse_odata_query(request)
    
    mock_students = [
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
        },
        {
            "studentID": "USER_002",
            "firstName": "Jane",
            "lastName": "Smith",
            "email": "jane.smith@company.com",
            "status": "Active",
            "department": "Marketing",
            "jobTitle": "Marketing Manager",
            "enrollmentDate": "2023-02-01T10:00:00Z",
            "lastLoginDate": "2024-01-13T16:45:00Z"
        },
        {
            "studentID": "USER_003",
            "firstName": "Bob",
            "lastName": "Johnson",
            "email": "bob.johnson@company.com",
            "status": "Active",
            "department": "Sales",
            "jobTitle": "Sales Representative",
            "enrollmentDate": "2023-03-10T11:00:00Z",
            "lastLoginDate": "2024-01-12T09:15:00Z"
        }
    ]
    
    if query_params['top']:
        mock_students = mock_students[:query_params['top']]
    
    return jsonify(create_odata_response(
        mock_students,
        "$metadata#Students",
        len(mock_students) if query_params['count'] else None
    ))

@sap_lms_bp.route('/learning/odatav4/public/admin/search-service/v1/Items', methods=['GET'])
def admin_search_items():
    """Search learning items (admin)"""
    query_params = parse_odata_query(request)
    mock_data = load_mock_data('catalog_courses.json')
    items = mock_data.get('value', [])
    
    if query_params['top']:
        items = items[:query_params['top']]
    
    return jsonify(create_odata_response(
        items,
        "$metadata#Items",
        len(items) if query_params['count'] else None
    ))

# User Assignment Service Data Endpoints
@sap_lms_bp.route('/learning/odatav4/public/user/userassignment-service/v1/UserPrograms', methods=['GET'])
def user_get_program_assignments_v1():
    """Get user program assignments v1"""
    query_params = parse_odata_query(request)
    
    mock_assignments = [
        {
            "assignmentID": "ASSIGN_001",
            "studentID": "USER_001",
            "programID": "PROG_001",
            "assignmentDate": "2024-01-01T09:00:00Z",
            "dueDate": "2024-08-30T17:00:00Z",
            "completionStatus": "In Progress",
            "assignedBy": "SUPERVISOR_001"
        },
        {
            "assignmentID": "ASSIGN_002",
            "studentID": "USER_001",
            "programID": "PROG_002",
            "assignmentDate": "2024-02-01T09:00:00Z",
            "dueDate": "2024-06-15T17:00:00Z",
            "completionStatus": "Not Started",
            "assignedBy": "SUPERVISOR_001"
        }
    ]
    
    if query_params['top']:
        mock_assignments = mock_assignments[:query_params['top']]
    
    return jsonify(create_odata_response(
        mock_assignments,
        "$metadata#UserPrograms",
        len(mock_assignments) if query_params['count'] else None
    ))

@sap_lms_bp.route('/learning/odatav4/public/user/userassignment-service/v2/itemAssignments', methods=['POST'])
def user_create_item_assignment_v2():
    """Create item assignment v2"""
    assignment_data = request.get_json()
    
    # Validate required fields
    required_fields = ['studentID', 'itemID']
    for field in required_fields:
        if field not in assignment_data:
            return jsonify({
                "error": {
                    "code": "MISSING_FIELD",
                    "message": f"Required field '{field}' is missing"
                }
            }), 400
    
    # Create response
    response_data = {
        "assignmentID": f"ASSIGN_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "studentID": assignment_data['studentID'],
        "itemID": assignment_data['itemID'],
        "assignmentDate": datetime.utcnow().isoformat() + "Z",
        "dueDate": assignment_data.get('dueDate'),
        "assignedBy": assignment_data.get('assignedBy', 'SYSTEM'),
        "priority": assignment_data.get('priority', 'Medium'),
        "status": "Active"
    }
    
    return jsonify(response_data), 201

@sap_lms_bp.route('/learning/odatav4/public/user/userassignment-service/v2/removeItemAssignments', methods=['POST'])
def user_remove_item_assignment_v2():
    """Remove item assignment v2"""
    removal_data = request.get_json()
    
    # Validate required fields
    required_fields = ['assignmentID']
    for field in required_fields:
        if field not in removal_data:
            return jsonify({
                "error": {
                    "code": "MISSING_FIELD",
                    "message": f"Required field '{field}' is missing"
                }
            }), 400
    
    # Create response
    response_data = {
        "assignmentID": removal_data['assignmentID'],
        "status": "removed",
        "removalReason": removal_data.get('removalReason', 'User request'),
        "removedDate": datetime.utcnow().isoformat() + "Z"
    }
    
    return jsonify(response_data), 200

# Financial Transactions Data Endpoints
@sap_lms_bp.route('/learning/odatav4/public/admin/financialtransactions/v1/FinancialTransactions', methods=['GET'])
def admin_get_financial_transactions():
    """Get financial transactions for admin operations"""
    query_params = parse_odata_query(request)
    
    mock_transactions = [
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
        },
        {
            "transactionID": "TXN_002",
            "orderNo": "ORD_2024_002",
            "studentID": "USER_002",
            "courseID": "COURSE_002",
            "amount": 499.99,
            "currency": "USD",
            "transactionType": "Purchase",
            "transactionDate": "2024-01-20T14:15:00Z",
            "status": "Completed",
            "paymentMethod": "Bank Transfer",
            "description": "Data Analysis with Python Course Purchase",
            "externalTransactionID": "EXT_TXN_12346"
        },
        {
            "transactionID": "TXN_003",
            "orderNo": "ORD_2024_003",
            "studentID": "USER_001",
            "courseID": "COURSE_001",
            "amount": 50.00,
            "currency": "USD",
            "transactionType": "Refund",
            "transactionDate": "2024-01-25T09:45:00Z",
            "status": "Completed",
            "paymentMethod": "Credit Card",
            "description": "Partial refund for Leadership Fundamentals Course",
            "externalTransactionID": "EXT_TXN_12347"
        }
    ]
    
    if query_params['top']:
        mock_transactions = mock_transactions[:query_params['top']]
    
    return jsonify(create_odata_response(
        mock_transactions,
        "$metadata#FinancialTransactions",
        len(mock_transactions) if query_params['count'] else None
    ))

# Error handling
@sap_lms_bp.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": {
            "code": "NOT_FOUND",
            "message": "The requested endpoint was not found"
        }
    }), 404

@sap_lms_bp.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": {
            "code": "INTERNAL_ERROR",
            "message": "An internal server error occurred"
        }
    }), 500


