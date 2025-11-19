# Project: Blog Post Creation with Sequential Agents

## Project Overview

This project is a Python application that demonstrates a multi-agent workflow for researching and summarizing a topic. It uses the Google Agent Development Kit (ADK) to create a sequence of agents that work together to answer a user's query.

The architecture consists of three main agents:
- **ResearchAgent**: Takes a user's topic, performs a Google search to gather relevant information.
- **SummarizerAgent**: Receives the research findings and creates a concise, bulleted summary.
- **ResearchCoordinator**: The root agent that orchestrates the workflow by first calling the `ResearchAgent` and then passing its findings to the `SummarizerAgent` to produce the final answer.

The core logic is contained within `agents/agents.py`.

## Building and Running

### 1. Setup Environment

The project uses a Python virtual environment located in the `.venv` directory. It can be automatically activated by sourcing the `.env.sh` script.

```bash
# Activate the virtual environment
source .env.sh
```

### 2. Install Dependencies

All required Python packages are listed in `requirements.txt`.

```bash
# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Key

The application requires a Google API key to function.
1. Create a file named `.env` in the root of the project.
2. Add your API key to the file:

```
GOOGLE_API_KEY="your_api_key_here"
```

### 4. Run the Application

The main script can be executed directly from the command line, providing a research topic as an argument.

```bash
# Run the agent workflow
python agents/agents.py "Your research topic here"
```

To see detailed logs of the agent's execution, you can use the `--debug` flag:

```bash
# Run in debug mode
python agents/agents.py "Your research topic here" --debug
```

## Development Conventions

- **Virtual Environment**: All dependencies are managed within the `.venv` virtual environment to avoid conflicts with system-wide packages.
- **Dependency Management**: Project dependencies are explicitly defined in `requirements.txt`.
- **Configuration**: API keys and other secrets are managed via a `.env` file and loaded using `python-dotenv`.
- **Asynchronous Code**: The main execution flow in `agents/agents.py` is asynchronous, using Python's `asyncio` library.
