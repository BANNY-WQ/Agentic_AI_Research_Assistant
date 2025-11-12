# Quick Start Guide - Agentic AI Research Assistant

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Web browser (Chrome, Firefox, Edge, etc.)

## Installation Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** If you encounter issues with specific packages, you can install them individually:
- `pip install fastapi uvicorn`
- `pip install langchain langchain-openai langchain-community`
- `pip install crewai`
- `pip install chromadb sentence-transformers`

### 2. Set Up Environment Variables

Run the setup script:
```bash
python setup.py
```

Or manually create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
VECTOR_DB_PATH=./data/vector_db
```

**Important:** 
- If you don't have an OpenAI API key, the system will use HuggingFace embeddings (free, but slower)
- The system will work without API keys using sample data, but functionality will be limited

### 3. Start the Backend Server

**Windows:**
```bash
start_backend.bat
```

**Linux/Mac:**
```bash
chmod +x start_backend.sh
./start_backend.sh
```

**Or manually:**
```bash
cd backend
python main.py
```

The backend will start on `http://localhost:8000`

### 4. Open the Frontend

Simply open `frontend/index.html` in your web browser.

**Or use a local server (recommended):**

**Python:**
```bash
cd frontend
python -m http.server 8080
```
Then open `http://localhost:8080` in your browser

**Node.js (if installed):**
```bash
cd frontend
npx http-server -p 8080
```

## Usage

### 1. Fill in Faculty Profile

1. Open the web interface
2. Fill in the Faculty Profile form:
   - **Department:** e.g., "Computer Science"
   - **Research Interests:** e.g., "Machine Learning, Natural Language Processing, Computer Vision"
   - **Expertise:** e.g., "Deep Learning, Neural Networks, Transformers"
3. Click "Start Analysis"

### 2. Search Research Papers

1. Enter a search query in the "Research Papers" section
2. Click "Search" or press Enter
3. View results with relevance scores

### 3. View Results

The system will display:
- **Research Papers:** Relevant papers with abstracts and metadata
- **Potential Collaborators:** Matched researchers with collaboration potential
- **Grant Opportunities:** Funding opportunities with deadlines and requirements

## API Endpoints

You can also use the API directly:

### Search Research
```bash
curl -X POST http://localhost:8000/api/research/search \
  -H "Content-Type: application/json" \
  -d '{"query": "machine learning", "max_results": 5}'
```

### Find Collaborators
```bash
curl -X POST http://localhost:8000/api/collaborators/find \
  -H "Content-Type: application/json" \
  -d '{
    "department": "Computer Science",
    "research_interests": ["Machine Learning", "NLP"],
    "expertise": ["Deep Learning", "Neural Networks"]
  }'
```

### Comprehensive Analysis
```bash
curl -X POST http://localhost:8000/api/comprehensive/analysis \
  -H "Content-Type: application/json" \
  -d '{
    "department": "Computer Science",
    "research_interests": ["Machine Learning", "NLP"],
    "expertise": ["Deep Learning", "Neural Networks"]
  }'
```

## Troubleshooting

### Backend won't start
- Check if port 8000 is available
- Verify Python version: `python --version` (should be 3.8+)
- Check if all dependencies are installed: `pip list`

### No results returned
- Check if `data/sample_data.json` exists
- Verify the backend is running: visit `http://localhost:8000`
- Check browser console for errors (F12)

### Import errors
- Make sure you're running from the correct directory
- Try: `cd backend && python -m main`

### Vector database errors
- Delete `data/vector_db` folder and restart
- The system will recreate it with sample data

## Features

✅ **Semantic Search** - Advanced search using LangChain
✅ **Collaborator Matching** - AI-powered partner discovery
✅ **Grant Discovery** - Automated funding opportunity identification
✅ **Animated UI** - Modern, responsive web interface
✅ **Real-time Results** - Fast API responses
✅ **Match Scoring** - Relevance and compatibility scores

## Next Steps

1. Add your OpenAI API key for better semantic search
2. Customize sample data in `data/sample_data.json`
3. Integrate with real research databases (ArXiv, PubMed)
4. Add user authentication
5. Implement result export features

## Support

For issues or questions:
1. Check the README.md for detailed documentation
2. Review PROJECT_PROMPT.md for implementation details
3. Check backend logs for error messages

Enjoy using the Agentic AI Research Assistant! 🚀

