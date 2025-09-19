# Government Internship Matcher - Vercel Deployment

This document explains how to deploy the Government Internship Matcher to Vercel.

## 📁 Project Structure for Vercel

```
sih2/
├── api/
│   ├── index.py            # Serverless Python API
│   └── requirements.txt    # Python dependencies for API
├── index.html              # Frontend entry point
├── styles.css              # Styling
├── script.js               # Frontend logic
├── package.json            # Node.js config (for Vercel detection)
├── vercel.json             # Vercel configuration
├── requirements.txt        # Root Python dependencies (local dev)
├── intern_ai_backend.py    # Local development server
├── match_utils.py          # Matching algorithm
└── README.md               # Documentation
```

## 🚀 Deployment Steps

### 1. Prerequisites
- [Vercel CLI](https://vercel.com/cli) installed: `npm i -g vercel`
- Git repository (GitHub, GitLab, or Bitbucket)

### 2. Deploy via Vercel CLI

```bash
# Login to Vercel
vercel login

# Navigate to project directory
cd sih2

# Deploy to Vercel
vercel

# Follow the prompts:
# ? Set up and deploy "sih2"? [Y/n] y
# ? Which scope do you want to deploy to? [Your Team]
# ? Link to existing project? [y/N] n
# ? What's your project's name? gov-internship-matcher
# ? In which directory is your code located? ./
```

### 3. Deploy via Vercel Dashboard

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your Git repository
4. Vercel will automatically detect the configuration
5. Click "Deploy"

## ⚙️ Configuration Files Explained

### `vercel.json`
Configures how Vercel handles your project:
- **Builds**: Defines how to build Python API and static files
- **Routes**: Routes API calls to serverless functions
- **Functions**: Configures Python runtime for the API

### `package.json`
Enables npm detection and provides metadata:
- Helps Vercel identify the project type
- Contains build scripts and project information

### `api/index.py`
Serverless function version of the Flask app:
- Optimized for Vercel's serverless environment
- Includes fallback matching logic if scikit-learn fails
- Additional endpoints for comprehensive API

### `api/requirements.txt`
Python dependencies specifically for the serverless function:
- Lighter version focusing on core dependencies
- Includes Werkzeug for WSGI compatibility

## 🔧 Environment Variables

If you need to add environment variables:

1. **Via Vercel CLI:**
   ```bash
   vercel env add VARIABLE_NAME
   ```

2. **Via Vercel Dashboard:**
   - Go to your project settings
   - Navigate to "Environment Variables"
   - Add your variables

## 🌐 Custom Domain

To use a custom domain:

1. **Via Vercel Dashboard:**
   - Go to your project
   - Click "Domains"
   - Add your custom domain
   - Configure DNS settings as instructed

## 📊 Monitoring & Analytics

Vercel provides built-in:
- **Analytics**: Track visitor data and performance
- **Speed Insights**: Monitor Core Web Vitals
- **Logs**: View function execution logs

Access these in your Vercel dashboard under your project.

## 🔍 Testing the Deployment

After deployment, test these endpoints:

- **Frontend**: `https://your-project.vercel.app`
- **Health Check**: `https://your-project.vercel.app/api/health`
- **Match Skills**: `POST https://your-project.vercel.app/api/match-skills`
- **All Internships**: `https://your-project.vercel.app/api/internships`

## 🐛 Troubleshooting

### Common Issues:

1. **Build Failures:**
   - Check `api/requirements.txt` for correct Python packages
   - Ensure all imports are available

2. **Function Timeout:**
   - Vercel has a 10-second timeout for Hobby plan
   - Optimize heavy computations or upgrade plan

3. **CORS Issues:**
   - Flask-CORS is configured in `api/index.py`
   - Check browser developer tools for specific errors

4. **Import Errors:**
   - The API includes fallback logic for `match_utils.py`
   - Scikit-learn might be heavy for serverless - fallback uses simple matching

### Logs and Debugging:

```bash
# View function logs
vercel logs [deployment-url]

# Local development with Vercel
vercel dev
```

## 🔄 Continuous Deployment

Vercel automatically deploys when you push to your Git repository:

1. **Connect Repository:** Link your GitHub/GitLab repo in Vercel dashboard
2. **Auto-Deploy:** Every push to main branch triggers deployment
3. **Preview Deployments:** Pull requests get preview URLs

## 💡 Optimization Tips

1. **Performance:**
   - Static files are served via Vercel's CDN
   - API functions are cached when possible

2. **Cost Optimization:**
   - Monitor function execution time
   - Use Vercel's analytics to optimize popular routes

3. **SEO:**
   - Add meta tags to `index.html`
   - Use Vercel's built-in SEO optimization

## 🔗 Useful Links

- [Vercel Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python)
- [Vercel Configuration](https://vercel.com/docs/project-configuration)
- [Flask on Vercel](https://vercel.com/guides/using-flask-with-vercel)

---

Your Government Internship Matcher is now ready for production deployment on Vercel! 🎉
