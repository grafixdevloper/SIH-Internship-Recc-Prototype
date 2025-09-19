# Government Internship Matcher - Frontend

A simple and intuitive web application that helps students find matching government internship opportunities based on their skills or resume.

## Features

### 🎯 Two Ways to Find Matches
1. **Skills Selection**: Choose from a comprehensive list of categorized skills
2. **Resume Upload**: Upload your resume and let AI analyze your skills automatically

### � Dark Mode Support
- Toggle between light and dark themes
- Dark theme features deep purple (`#231054`) color scheme
- Theme preference saved automatically
- Smooth transitions between themes

### �🏛️ Government Ministry Internships
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
├── api/
│   ├── index.py            # Serverless Python API for Vercel
│   └── requirements.txt    # Python dependencies for serverless
├── index.html              # Main HTML file with dark mode toggle
├── styles.css              # CSS styling with theme variables
├── script.js               # JavaScript functionality with theme management
├── intern_ai_backend.py    # Flask backend API (local development)
├── match_utils.py          # AI matching algorithm
├── package.json            # Node.js config for Vercel deployment
├── vercel.json             # Vercel deployment configuration
├── requirements.txt        # Python dependencies (local development)
├── DEPLOYMENT.md           # Vercel deployment guide
└── README.md               # This file
```

## How to Run

### Local Development

#### Prerequisites
- Python 3.7 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)

#### Option A: Using pip (Recommended)
```bash
# Navigate to project directory
cd sih2

# Install required Python packages
pip install -r requirements.txt

# Start the backend server
python intern_ai_backend.py
```

#### Option B: Manual Installation
```bash
# Install packages individually if requirements.txt fails
pip install Flask==2.3.3
pip install Flask-CORS==4.0.0
pip install scikit-learn==1.3.0
pip install numpy

# Start the backend server
python intern_ai_backend.py
```

The backend will start at `http://localhost:5000`

#### Frontend Setup

Simply open `index.html` in your web browser, or use a local server:

##### Option A: Direct File Opening
```bash
# Simply double-click index.html or open in browser
# File path: file:///path/to/sih2/index.html
```

##### Option B: Local Server (Recommended for full functionality)
```bash
# Using Python's built-in server
python -m http.server 8080
# Then visit: http://localhost:8080

# Or using Node.js http-server (if installed)
npx http-server
# Then visit: http://localhost:8080
```

**Note**: Using a local server is recommended to avoid CORS issues when making API calls.

### 🚀 Production Deployment (Vercel)

For production deployment on Vercel:

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy to Vercel
vercel

# Or deploy via GitHub integration
# 1. Push code to GitHub repository
# 2. Connect repository to Vercel dashboard
# 3. Automatic deployment on every push
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

#### Quick Vercel Deployment

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/your-username/gov-internship-matcher)

**Features of Vercel deployment:**
- ✅ Automatic HTTPS and custom domains
- ✅ Serverless Python API functions  
- ✅ Global CDN for fast loading
- ✅ Automatic deployments from Git
- ✅ Preview deployments for pull requests

## How to Use

### Method 1: Skills Selection
1. Click on the "Select Skills" tab
2. Choose skills from categorized lists:
   - Programming & Development (Python, JavaScript, React, etc.)
   - Data Science & AI (Machine Learning, Deep Learning, etc.)
   - Design & UI/UX (Figma, Adobe Creative Suite, etc.)
   - Business & Management (Project Management, Communication, etc.)
3. Click "Find My Matches" to get recommendations

### Method 2: Resume Upload
1. Click on the "Upload Resume" tab
2. Drag & drop your resume or click to browse
3. Supported formats: PDF, DOC, DOCX, TXT (max 10MB)
4. Click "Analyze Resume & Find Matches"

### Theme Toggle
- Click the moon/sun icon in the header to switch between light and dark themes
- Your theme preference is automatically saved

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
- **HTML5**: Semantic markup with accessibility features
- **CSS3**: Modern styling with CSS custom properties (variables)
  - CSS Grid and Flexbox for responsive layouts
  - Gradient backgrounds and smooth animations
  - Dark/light theme system using CSS variables
- **JavaScript (Vanilla)**: 
  - Theme management with localStorage persistence
  - File upload handling and validation
  - REST API communication
  - Dynamic UI updates

### Backend  
- **Python Flask**: Lightweight REST API server
- **Flask-CORS**: Cross-origin resource sharing support
- **scikit-learn**: Machine learning library for TF-IDF and cosine similarity
- **NumPy**: Numerical computing support

### Dependencies (requirements.txt)
```
Flask==2.3.3          # Web framework
Flask-CORS==4.0.0     # CORS support  
scikit-learn==1.3.0   # ML algorithms
numpy>=1.21.0         # Numerical operations
```

## Browser Support

- Chrome 60+
- Firefox 55+  
- Safari 12+
- Edge 79+

## Future Enhancements

- [ ] Real resume parsing using NLP libraries (spaCy, NLTK)
- [ ] User authentication and profile management
- [ ] Save favorite internships and application tracking
- [ ] Advanced filtering options (location, duration, stipend)
- [ ] Email notifications for new matching opportunities
- [ ] Integration with actual government internship portals
- [ ] System theme detection (auto dark/light mode)
- [ ] Multi-language support for wider accessibility
- [ ] Mobile app version using Progressive Web App (PWA)
- [ ] Analytics dashboard for internship coordinators

## Troubleshooting

### Common Issues

1. **CORS Error**: If you see CORS errors, make sure to:
   - Run the frontend through a local server (not file://)
   - Ensure Flask-CORS is installed: `pip install Flask-CORS`

2. **Module Not Found**: If Python modules are missing:
   ```bash
   pip install -r requirements.txt
   ```

3. **Port Already in Use**: If port 5000 is occupied:
   ```python
   # In intern_ai_backend.py, change the last line to:
   app.run(debug=True, port=5001)
   # Then update API_BASE_URL in script.js to http://localhost:5001
   ```

4. **Dark Mode Not Saving**: Clear browser cache and localStorage:
   - Open Developer Tools (F12)
   - Go to Application/Storage tab
   - Clear localStorage for your domain

## Contributing

This project was created for the Smart India Hackathon. Feel free to contribute by:
- Adding more government internship opportunities
- Improving the skill matching algorithm
- Enhancing the UI/UX design
- Adding new features

---

Made with ❤️ for Smart India Hackathon 2024
