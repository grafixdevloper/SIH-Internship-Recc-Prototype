from flask import Flask, jsonify
from flask_cors import CORS
from match_utils import calculate_matches

app = Flask(__name__)
CORS(app)

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

@app.route('/api/match-skills', methods=['POST'])
def match_skills():
    from flask import request
    data = request.json
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

if __name__ == "__main__":
    app.run(debug=True)
