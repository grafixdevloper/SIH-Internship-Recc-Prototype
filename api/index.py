from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os

# Add the parent directory to Python path to import match_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from match_utils import calculate_matches
    print("Successfully imported match_utils")
except ImportError as e:
    print(f"Failed to import match_utils: {e}")
    # Fallback if match_utils is not available
    def calculate_matches(student_profile, internships):
        # Simple fallback matching logic
        results = []
        student_skills = set(skill.lower() for skill in student_profile.get("skills", []))
        
        for internship in internships:
            required_skills = set(skill.lower() for skill in internship.get("required_skills", []))
            
            # Calculate simple overlap percentage
            if required_skills:
                overlap = len(student_skills.intersection(required_skills))
                match_score = (overlap / len(required_skills)) * 100
            else:
                match_score = 0
            
            internship_copy = internship.copy()
            internship_copy["match_score"] = match_score
            results.append(internship_copy)
        
        # Sort by match score (descending)
        results.sort(key=lambda x: x["match_score"], reverse=True)
        return results

app = Flask(__name__)
CORS(app, origins=["*"], methods=["GET", "POST", "OPTIONS"], allow_headers=["Content-Type", "Authorization"])

# Add explicit OPTIONS handling for preflight requests
@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = jsonify({})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response

# In-memory data
ALL_STUDENTS = [
    {
        "id": "1",
        "name": "Priya Sharma",
        "skills": ["Python", "Data Analysis", "React", "Project Management"],
    },
    {
        "id": "2",
        "name": "Aman Verma",
        "skills": ["Python", "Machine Learning", "Deep Learning"],
    },
    {
        "id": "3",
        "name": "Sneha Patel",
        "skills": ["React", "JavaScript", "UI/UX"],
    },
]

ALL_INTERNSHIPS = [
    {
        "id": 1,
        "title": "Data Science Intern",
        "ministry": "Ministry of Electronics and Information Technology",
        "location": "New Delhi",
        "required_skills": ["Python", "Data Analysis", "Machine Learning"],
    },
    {
        "id": 2,
        "title": "Frontend Developer Intern",
        "ministry": "Ministry of Education",
        "location": "Bangalore",
        "required_skills": ["React", "JavaScript", "UI/UX"],
    },
    {
        "id": 3,
        "title": "AI Research Intern",
        "ministry": "Ministry of Science & Technology",
        "location": "Hyderabad",
        "required_skills": ["Python", "Deep Learning", "Research"],
    },
    {
        "id": 4,
        "title": "Project Management Intern",
        "ministry": "Ministry of Corporate Affairs",
        "location": "Mumbai",
        "required_skills": ["Project Management", "Communication", "Excel"],
    },
    {
        "id": 5,
        "title": "Cybersecurity Intern",
        "ministry": "Ministry of Home Affairs",
        "location": "New Delhi",
        "required_skills": ["Cybersecurity", "Python", "Networking"],
    },
    {
        "id": 6,
        "title": "Digital Marketing Intern",
        "ministry": "Ministry of Information & Broadcasting",
        "location": "Mumbai",
        "required_skills": ["Digital Marketing", "Social Media", "Content Writing"],
    },
    {
        "id": 7,
        "title": "Web Development Intern",
        "ministry": "National Informatics Centre",
        "location": "Pune",
        "required_skills": ["HTML", "CSS", "JavaScript", "React"],
    },
    {
        "id": 8,
        "title": "Data Analytics Intern",
        "ministry": "Ministry of Statistics & Programme Implementation",
        "location": "Chennai",
        "required_skills": ["Data Analysis", "Excel", "SQL", "Statistics"],
    },
]

# Mock data for candidates
candidates = [
    {
        "id": 1,
        "name": "Aman Verma",
        "university": "IIT Delhi",
        "match_score": 98,
    },
    {
        "id": 2,
        "name": "Sneha Patel",
        "university": "BITS Pilani",
        "match_score": 95,
    },
    {
        "id": 3,
        "name": "Rahul Singh",
        "university": "NIT Trichy",
        "match_score": 93,
    },
    {
        "id": 4,
        "name": "Meera Nair",
        "university": "VIT Vellore",
        "match_score": 91,
    },
]

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint for Vercel"""
    return jsonify({
        "status": "healthy", 
        "message": "Gov Internship Matcher API is running",
        "timestamp": "2024-09-19",
        "version": "1.0.0"
    })

@app.route('/api/test', methods=['GET', 'POST'])
def test_endpoint():
    """Simple test endpoint"""
    if request.method == 'POST':
        data = request.get_json() or {}
        return jsonify({
            "method": "POST",
            "received_data": data,
            "message": "POST test successful"
        })
    else:
        return jsonify({
            "method": "GET", 
            "message": "GET test successful",
            "api_working": True
        })

@app.route('/api/recommendations/<student_id>', methods=['GET'])
def get_recommendations(student_id):
    student = next((s for s in ALL_STUDENTS if s["id"] == student_id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    
    # Use AI match function
    scored = calculate_matches(student, [dict(i) for i in ALL_INTERNSHIPS])
    
    # Add back id, title, ministry, location, required_skills, match_score only
    result = [
        {
            "id": i["id"],
            "title": i["title"],
            "ministry": i["ministry"],
            "location": i["location"],
            "required_skills": i["required_skills"],
            "match_score": i["match_score"],
        }
        for i in scored
    ]
    return jsonify(result)

@app.route('/api/candidates/<internship_id>', methods=['GET'])
def get_candidates(internship_id):
    return jsonify(candidates)

@app.route('/api/match-skills', methods=['POST', 'OPTIONS'])
def match_skills():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
        
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
            
        skills = data.get('skills', [])
        
        if not skills:
            return jsonify({"error": "No skills provided"}), 400
        
        # Create a mock student profile with the provided skills
        student_profile = {"skills": skills}
        
        # Use AI match function
        scored = calculate_matches(student_profile, [dict(i) for i in ALL_INTERNSHIPS])
        
        # Add back id, title, ministry, location, required_skills, match_score only
        result = [
            {
                "id": i["id"],
                "title": i["title"],
                "ministry": i["ministry"],
                "location": i["location"],
                "required_skills": i["required_skills"],
                "match_score": i["match_score"],
            }
            for i in scored
        ]
        
        return jsonify(result)
        
    except Exception as e:
        print(f"Error in match_skills: {str(e)}")
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route('/api/internships', methods=['GET'])
def get_all_internships():
    """Get all available internships"""
    return jsonify(ALL_INTERNSHIPS)

@app.route('/api/students', methods=['GET'])
def get_all_students():
    """Get all students (for admin purposes)"""
    return jsonify(ALL_STUDENTS)

# For Vercel serverless functions
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Vercel handler function
app.wsgi_app = app.wsgi_app

def handler(environ, start_response):
    return app(environ, start_response)

# Export for Vercel
def app_handler(environ, start_response):
    return app(environ, start_response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
