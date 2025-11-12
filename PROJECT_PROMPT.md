# Agentic AI Research Assistant - Complete Project Prompt

## Project Overview

Create a comprehensive **Agentic AI Research Assistant** for faculty members that leverages **LangChain** for semantic search across research databases and **CrewAI** for identifying potential collaborators and grant opportunities. The system should analyze faculty research interests and expertise to suggest relevant partnerships and funding calls, streamlining the research process.

## Core Requirements

### 1. Backend Architecture (Python/FastAPI)

#### 1.1 Semantic Search Service (LangChain)
- Implement semantic search using LangChain's vector store capabilities
- Support multiple embedding models (OpenAI, HuggingFace fallback)
- Vector database integration (ChromaDB)
- Search across research paper databases
- Return results with relevance scores and metadata

#### 1.2 Research Agent
- Agent responsible for research paper discovery
- Integrates with semantic search service
- Enhances queries with research interests
- Returns formatted research results with:
  - Title, authors, abstract
  - Publication date, venue
  - Relevance score
  - Keywords
  - URL links

#### 1.3 Collaborator Agent (CrewAI)
- Use CrewAI to create intelligent collaborator matching agent
- Analyze faculty research profiles
- Match based on:
  - Research interest overlap
  - Complementary expertise
  - Department and institution
- Calculate match scores
- Provide collaboration potential assessment
- Return collaborator profiles with contact information

#### 1.4 Grant Agent (CrewAI)
- Use CrewAI to create grant discovery agent
- Match grant opportunities with research profiles
- Consider:
  - Research area alignment
  - Eligibility requirements
  - Funding amounts and deadlines
- Calculate match scores
- Return grant details with application requirements

#### 1.5 API Endpoints (FastAPI)
- `POST /api/research/search` - Semantic research search
- `POST /api/collaborators/find` - Find potential collaborators
- `POST /api/grants/discover` - Discover grant opportunities
- `POST /api/comprehensive/analysis` - Complete analysis (all three)
- `GET /` - Health check

### 2. Frontend (HTML/CSS/JavaScript)

#### 2.1 User Interface
- Modern, responsive design
- Dark theme with gradient accents
- Animated background particles
- Smooth scroll animations
- Interactive cards and forms

#### 2.2 Features
- Faculty profile input form:
  - Name, department
  - Research interests (comma-separated)
  - Areas of expertise (comma-separated)
- Research search interface
- Results display sections:
  - Research papers with relevance scores
  - Collaborator matches with match percentages
  - Grant opportunities with deadlines
- Loading states and animations
- Error handling and user feedback

#### 2.3 Animations
- Floating particles in background
- Fade-in animations on page load
- Slide-in animations for cards
- Hover effects on interactive elements
- Loading spinners
- Smooth transitions

### 3. Data Management

#### 3.1 Sample Data
- Research papers database (JSON)
- Collaborator profiles database
- Grant opportunities database
- Include realistic sample data for demonstration

#### 3.2 Vector Database
- ChromaDB for semantic search
- Persistent storage
- Automatic data loading

### 4. Configuration

#### 4.1 Environment Variables
- OpenAI API key
- Anthropic API key (optional)
- Vector database path
- External API keys (ArXiv, PubMed, etc.)

#### 4.2 Dependencies
- FastAPI for backend
- LangChain for semantic search
- CrewAI for agent orchestration
- ChromaDB for vector storage
- Pydantic for data validation

## Technical Specifications

### Backend Structure
```
backend/
├── main.py                 # FastAPI application entry point
├── agents/
│   ├── research_agent.py   # Research search agent
│   ├── collaborator_agent.py # Collaborator matching agent
│   └── grant_agent.py      # Grant discovery agent
├── services/
│   ├── semantic_search.py  # LangChain semantic search service
│   └── data_processor.py   # Data processing utilities
└── models/
    └── schemas.py          # Pydantic models for API
```

### Frontend Structure
```
frontend/
├── index.html              # Main HTML file
├── styles.css              # Styling with animations
└── app.js                  # Frontend JavaScript logic
```

### Data Structure
```
data/
├── sample_data.json        # Sample research data
└── vector_db/              # ChromaDB storage
```

## Implementation Details

### Semantic Search Implementation
- Use LangChain's embedding models
- Create vector store from research papers
- Implement similarity search
- Return top-k results with scores
- Extract keywords from results

### CrewAI Agent Implementation
- Create specialized agents for each task
- Define agent roles, goals, and backstories
- Implement matching algorithms
- Calculate relevance/match scores
- Return structured results

### API Design
- RESTful API design
- JSON request/response format
- Error handling
- CORS enabled for frontend
- Async/await for performance

### Frontend Design
- Single-page application
- AJAX for API calls
- Dynamic content rendering
- Responsive layout
- Accessibility considerations

## Features to Implement

1. **Semantic Research Search**
   - Query enhancement with research interests
   - Multi-database search capability
   - Relevance scoring
   - Keyword extraction

2. **Collaborator Discovery**
   - Profile matching algorithm
   - Interest overlap calculation
   - Expertise complementarity analysis
   - Collaboration potential assessment

3. **Grant Opportunity Discovery**
   - Keyword-based matching
   - Eligibility checking
   - Deadline tracking
   - Application requirements listing

4. **Comprehensive Analysis**
   - Parallel execution of all agents
   - Combined results presentation
   - Summary statistics

5. **User Experience**
   - Smooth animations
   - Loading indicators
   - Error messages
   - Empty states
   - Result cards with metadata

## Testing Considerations

- Test API endpoints
- Verify semantic search accuracy
- Test matching algorithms
- Validate data formats
- Check error handling

## Deployment

- Backend runs on port 8000
- Frontend can be served statically
- Environment variables for configuration
- Vector database persistence

## Success Criteria

✅ Semantic search returns relevant research papers
✅ Collaborator matching finds appropriate partners
✅ Grant discovery identifies relevant opportunities
✅ Web interface is responsive and animated
✅ All API endpoints work correctly
✅ Error handling is robust
✅ Code is well-structured and documented

## Additional Enhancements (Optional)

- Export results to PDF/CSV
- Save favorite collaborators/grants
- Email notifications for new opportunities
- Integration with real research databases (ArXiv, PubMed)
- User authentication and profiles
- Advanced filtering options
- Recommendation history

---

This prompt provides a complete specification for building a professional Agentic AI Research Assistant that combines LangChain's semantic search capabilities with CrewAI's agent orchestration to help faculty members discover research opportunities, find collaborators, and identify grant funding.

