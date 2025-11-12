# 🚀 Project is Running!

## 📍 Localhost URLs

### Backend API Server
**URL:** http://localhost:8000

**API Documentation:** http://localhost:8000/docs (Swagger UI)

**Health Check:** http://localhost:8000/

### Frontend Web Interface

**Option 1: Direct File (Easiest)**
- Navigate to: `frontend/index.html`
- Double-click to open in browser
- **Note:** For full functionality, use Option 2 or 3

**Option 2: Python HTTP Server (Recommended)**
```powershell
cd frontend
python -m http.server 8080
```
Then open: **http://localhost:8080**

**Option 3: VS Code Live Server**
- Right-click `frontend/index.html`
- Select "Open with Live Server"
- Usually opens on: **http://127.0.0.1:5500**

## ✅ Quick Test

1. **Test Backend:**
   - Open: http://localhost:8000/
   - Should see: `{"status":"online","service":"Agentic AI Research Assistant","version":"1.0.0"}`

2. **Test Frontend:**
   - Open the frontend using one of the options above
   - Fill in the faculty profile form
   - Click "Start Analysis"

## 🎯 How to Use

1. **Open Frontend** (use one of the URLs above)
2. **Fill Faculty Profile:**
   - Department: "Computer Science"
   - Research Interests: "Machine Learning, Natural Language Processing"
   - Expertise: "Deep Learning, Neural Networks"
3. **Click "Start Analysis"**
4. **View Results:**
   - Research Papers
   - Potential Collaborators
   - Grant Opportunities

## 🔧 If Backend Not Running

If http://localhost:8000/ doesn't work:

1. **Start backend manually:**
   ```powershell
   cd backend
   python main.py
   ```

2. **Check for errors** in the terminal

3. **Verify dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

## 📝 Notes

- Backend runs on **port 8000**
- Frontend can run on any port (8080, 5500, etc.)
- Make sure backend is running before using frontend
- The system works with sample data (no API keys required)

---

**Backend:** http://localhost:8000  
**Frontend:** http://localhost:8080 (if using Python server) or open `frontend/index.html` directly

Enjoy! 🎉

