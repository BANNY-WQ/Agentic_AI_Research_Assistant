# How to Run the Project

## ✅ Backend Server Status

The backend server should be starting in the background. 

## 🚀 Quick Start Instructions

### Step 1: Verify Backend is Running

Open a new terminal and check:
```powershell
curl http://localhost:8000/
```

Or open in browser: http://localhost:8000/

You should see:
```json
{
  "status": "online",
  "service": "Agentic AI Research Assistant",
  "version": "1.0.0"
}
```

### Step 2: Open the Frontend

**Option 1: Direct File Open (Easiest)**
- Navigate to the `frontend` folder
- Double-click `index.html`
- It will open in your default browser

**Option 2: Using Python HTTP Server (Recommended)**
```powershell
cd frontend
python -m http.server 8080
```
Then open: http://localhost:8080

**Option 3: Using Live Server (if you have VS Code)**
- Right-click on `index.html`
- Select "Open with Live Server"

### Step 3: Use the Application

1. **Fill in Faculty Profile:**
   - Department: e.g., "Computer Science"
   - Research Interests: e.g., "Machine Learning, Natural Language Processing"
   - Expertise: e.g., "Deep Learning, Neural Networks"
   - Click "Start Analysis"

2. **Search Research Papers:**
   - Enter a search query
   - Click "Search" button

3. **View Results:**
   - Research Papers with relevance scores
   - Potential Collaborators with match percentages
   - Grant Opportunities with deadlines

## 🔧 Troubleshooting

### If Backend Won't Start:

1. **Check if port 8000 is in use:**
   ```powershell
   netstat -ano | findstr :8000
   ```

2. **Start backend manually:**
   ```powershell
   cd backend
   python main.py
   ```

3. **Check for errors:**
   - Look for import errors
   - Verify all dependencies are installed: `pip install -r requirements.txt`

### If Frontend Can't Connect:

1. **Check backend is running:**
   - Visit http://localhost:8000/ in browser
   - Should see JSON response

2. **Check browser console (F12):**
   - Look for CORS errors
   - Check network tab for failed requests

3. **Update API URL in frontend/app.js:**
   - Line 2: `const API_BASE_URL = 'http://localhost:8000';`
   - Make sure it matches your backend URL

## 📝 Notes

- The system works without API keys using sample data
- For better semantic search, add OpenAI API key to `.env` file
- Sample data is loaded from `data/sample_data.json`
- Vector database is created automatically in `data/vector_db/`

## 🎯 Testing the API

You can test the API directly using curl or Postman:

```powershell
# Test health endpoint
curl http://localhost:8000/

# Test research search
curl -X POST http://localhost:8000/api/research/search -H "Content-Type: application/json" -d '{\"query\": \"machine learning\", \"max_results\": 5}'
```

Enjoy using the Agentic AI Research Assistant! 🚀

