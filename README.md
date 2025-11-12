# Agentic AI Research Assistant for Faculty

A comprehensive AI-powered research assistant that helps faculty members discover research opportunities, find collaborators, and identify grant funding using LangChain for semantic search and CrewAI for intelligent agent orchestration.

## Features

- **Semantic Research Search**: Advanced semantic search across research databases using LangChain
- **Collaborator Discovery**: AI-powered matching of potential research collaborators based on expertise and interests
- **Grant Opportunity Identification**: Automated discovery of relevant funding opportunities
- **Research Interest Analysis**: Deep analysis of faculty research profiles and expertise
- **Interactive Web Interface**: Modern, animated web UI with real-time search and recommendations
- **Multi-Agent System**: CrewAI agents working collaboratively to provide comprehensive research assistance

## Tech Stack

- **Backend**: Python, FastAPI, LangChain, CrewAI
- **Frontend**: HTML5, CSS3, JavaScript (with animations)
- **AI/ML**: OpenAI/Anthropic APIs, Vector Databases
- **Data**: Research databases, grant databases, faculty profiles

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Run the application:
```bash
# Start backend
python backend/main.py

# Open frontend/index.html in browser
```

## Project Structure

```
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── agents/
│   │   ├── research_agent.py  # Research search agent
│   │   ├── collaborator_agent.py # Collaborator discovery agent
│   │   └── grant_agent.py      # Grant opportunity agent
│   ├── services/
│   │   ├── semantic_search.py  # LangChain semantic search
│   │   └── data_processor.py   # Data processing utilities
│   └── models/
│       └── schemas.py          # Pydantic models
├── frontend/
│   ├── index.html              # Main web interface
│   ├── styles.css              # Styling with animations
│   └── app.js                  # Frontend logic
├── data/
│   └── sample_data.json        # Sample research data
└── requirements.txt            # Python dependencies
```

## Usage

1. Enter your research interests and expertise
2. The system will:
   - Search relevant research papers and publications
   - Identify potential collaborators
   - Discover matching grant opportunities
3. Review recommendations and export results

## License

MIT License

