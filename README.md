# Government Internship Matcher - Frontend

A simple and intuitive web application that helps students find matching government internship opportunities based on their skills or resume.

## Features

### 🎯 Two Ways to Find Matches
1. **Skills Selection**: Choose from a comprehensive list of categorized skills
2. **Resume Upload**: Upload your resume and let AI analyze your skills automatically

### 🏛️ Government Ministry Internships
- Ministry of Electronics and Information Technology (MeitY)
- Ministry of Education  
- Ministry of Science & Technology
- Ministry of Corporate Affairs
- And more...

### 🤖 AI-Powered Matching
- Uses TF-IDF vectorization and cosine similarity
- Provides percentage match scores
- Ranks internships by compatibility

## Files Structure

```
sih2/
├── index.html          # Main HTML file
├── styles.css          # CSS styling
├── script.js           # JavaScript functionality
├── intern_ai_backend.py # Flask backend API
├── match_utils.py      # AI matching algorithm
└── README.md           # This file
```

## How to Run

### 1. Start the Backend Server

Make sure Python is installed, then run:

```bash
# Install required Python packages
pip install flask flask-cors scikit-learn

# Start the backend server
python intern_ai_backend.py
```

The backend will start at `http://localhost:5000`

### 2. Open the Frontend

Simply open `index.html` in your web browser, or use a local server:

```bash
# Using Python's built-in server
python -m http.server 8080

# Or using Node.js http-server (if installed)
npx http-server
```

Then visit `http://localhost:8080`

## How to Use

### Method 1: Skills Selection
1. Click on the "Select Skills" tab
2. Choose skills from categorized lists:
   - Programming & Development
   - Data Science & AI  
   - Design & UI/UX
   - Business & Management
3. Click "Find My Matches" to get recommendations

### Method 2: Resume Upload
1. Click on the "Upload Resume" tab
2. Drag & drop your resume or click to browse
3. Supported formats: PDF, DOC, DOCX, TXT
4. Click "Analyze Resume & Find Matches"

## API Endpoints

The backend provides these endpoints:

- `GET /api/recommendations/<student_id>` - Get matches for a specific student
- `GET /api/candidates/<internship_id>` - Get candidates for an internship
- `POST /api/match-skills` - Get matches based on provided skills array

### Example API Usage

```javascript
// Find matches for selected skills
fetch('http://localhost:5000/api/match-skills', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ 
        skills: ['Python', 'Data Analysis', 'Machine Learning'] 
    })
})
```

## Customization

### Adding New Skills
Edit the skill categories in `index.html` and add corresponding entries to the backend skill matching logic.

### Adding New Internships
Modify the `ALL_INTERNSHIPS` array in `intern_ai_backend.py`.

### Styling
Customize the appearance by editing `styles.css`. The design uses:
- CSS Grid and Flexbox for layout
- Gradient backgrounds
- Smooth animations and transitions
- Responsive design for mobile devices

## Technology Stack

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript**: Vanilla JS for interactivity and API communication

### Backend  
- **Python Flask**: REST API server
- **scikit-learn**: TF-IDF vectorization and cosine similarity
- **Flask-CORS**: Cross-origin resource sharing

## Browser Support

- Chrome 60+
- Firefox 55+  
- Safari 12+
- Edge 79+

## Future Enhancements

- [ ] Real resume parsing using NLP libraries
- [ ] User authentication and profiles
- [ ] Save favorite internships
- [ ] Advanced filtering options
- [ ] Email notifications for new matches
- [ ] Integration with government internship portals

## Contributing

This project was created for the Smart India Hackathon. Feel free to contribute by:
- Adding more government internship opportunities
- Improving the skill matching algorithm
- Enhancing the UI/UX design
- Adding new features

---

Made with ❤️ for Smart India Hackathon 2024
