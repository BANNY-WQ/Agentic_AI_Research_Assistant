# 🌐 Localhost URLs - Agentic AI Research Assistant

## ✅ Backend Server

**Main API Server:**
```
http://localhost:8000
```

**API Documentation (Swagger):**
```
http://localhost:8000/docs
```

**Alternative Docs (ReDoc):**
```
http://localhost:8000/redoc
```

**Health Check:**
```
http://localhost:8000/
```
Expected response:
```json
{
  "status": "online",
  "service": "Agentic AI Research Assistant",
  "version": "1.0.0"
}
```

---

## 🎨 Frontend Web Interface

### Option 1: Direct File Open (Easiest)
1. Navigate to `frontend` folder
2. Double-click `index.html`
3. It will open in your default browser

### Option 2: Python HTTP Server (Recommended)
Open a new terminal and run:
```powershell
cd frontend
python -m http.server 8080
```
Then open in browser:
```
http://localhost:8080
```

### Option 3: VS Code Live Server
If you have VS Code with Live Server extension:
1. Right-click on `frontend/index.html`
2. Select "Open with Live Server"
3. Usually opens on: `http://127.0.0.1:5500`

---

## 🚀 Quick Start Guide

### Step 1: Start Backend
The backend server should already be running. If not:
- Double-click `START_SERVER.bat` (Windows)
- Or run: `cd backend && python main.py`

### Step 2: Open Frontend
- Open `frontend/index.html` in your browser
- Or use Python HTTP server (Option 2 above)

### Step 3: Use the Application
1. Fill in the **Faculty Profile** form:
   - Department: e.g., "Computer Science"
   - Research Interests: e.g., "Machine Learning, Natural Language Processing"
   - Expertise: e.g., "Deep Learning, Neural Networks"
2. Click **"Start Analysis"**
3. View results:
   - Research Papers
   - Potential Collaborators
   - Grant Opportunities

---

## 🧪 Test the API

### Using Browser:
Open: http://localhost:8000/

### Using PowerShell:
```powershell
Invoke-WebRequest -Uri "http://localhost:8000/" -UseBasicParsing
```

### Using curl:
```powershell
curl http://localhost:8000/
```

---

## 📝 API Endpoints

All endpoints are available at: `http://localhost:8000`

- `GET /` - Health check
- `POST /api/research/search` - Search research papers
- `POST /api/collaborators/find` - Find collaborators
- `POST /api/grants/discover` - Discover grants
- `POST /api/comprehensive/analysis` - Full analysis

---

## ⚠️ Troubleshooting

### Backend not starting?
1. Check if port 8000 is available
2. Make sure all dependencies are installed: `pip install -r requirements.txt`
3. Check for errors in the terminal

### Frontend can't connect?
1. Verify backend is running: http://localhost:8000/
2. Check browser console (F12) for errors
3. Make sure API URL in `frontend/app.js` is: `http://localhost:8000`

### CORS errors?
- Backend has CORS enabled for all origins
- If issues persist, check `backend/main.py` CORS settings

---

## 🎯 Current Status

✅ Backend server: **Running on http://localhost:8000**
✅ Frontend: **Ready to open**
✅ Sample data: **Loaded**
✅ Vector database: **Initialized**

---

**Enjoy using the Agentic AI Research Assistant!** 🚀

