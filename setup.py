"""
Setup script for Agentic AI Research Assistant
"""

import os
from pathlib import Path

def create_env_file():
    """Create .env file from template if it doesn't exist"""
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if not env_file.exists():
        if env_example.exists():
            # Copy example to .env
            with open(env_example, 'r') as f:
                content = f.read()
            with open(env_file, 'w') as f:
                f.write(content)
            print("Created .env file from .env.example")
        else:
            # Create basic .env file
            env_content = """# OpenAI API Key (for LangChain)
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic API Key (optional, for Claude)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Vector Database Path
VECTOR_DB_PATH=./data/vector_db

# Research Database API Keys (if using external APIs)
ARXIV_API_KEY=
PUBMED_API_KEY=
GRANT_DB_API_KEY=
"""
            with open(env_file, 'w') as f:
                f.write(env_content)
            print("Created .env file. Please add your API keys")
        print("WARNING: Please edit .env file and add your API keys before running the application")
    else:
        print(".env file already exists")

def create_directories():
    """Create necessary directories"""
    directories = [
        "data/vector_db",
        "backend/agents",
        "backend/services",
        "backend/models",
        "frontend"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    print("Created necessary directories")

if __name__ == "__main__":
    print("Setting up Agentic AI Research Assistant...")
    create_directories()
    create_env_file()
    print("\n✅ Setup complete!")
    print("\nNext steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Edit .env file and add your API keys")
    print("3. Run backend: cd backend && python main.py")
    print("4. Open frontend/index.html in your browser")

