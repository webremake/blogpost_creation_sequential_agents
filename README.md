# Blog Post Creation with Sequential Agents

This project demonstrates a multi-agent workflow for researching a topic and generating a concise summary using the Google Agent Development Kit (ADK).

## Overview

The application uses a sequence of AI agents to answer a user's query. The workflow is orchestrated by a root agent that coordinates the tasks of specialized sub-agents:

1.  **ResearchAgent**: Takes a user's topic and uses Google Search to gather relevant information.
2.  **SummarizerAgent**: Receives the research findings and creates a clear, bulleted summary.
3.  **ResearchCoordinator**: The main agent that manages the workflow, calling the research agent first and then passing its findings to the summarizer to produce the final answer.

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.12.2 or higher
- `pip` for package management

### 1. Clone the Repository

```bash
git clone https://github.com/webremake/blogpost_creation_sequential_agents.git
cd blogpost_creation_sequential_agents
```

### 2. Set Up the Environment

This project uses a Python virtual environment to manage dependencies. A helper script is provided to activate it.

```bash
# Activate the virtual environment
source .env.sh
```

### 3. Install Dependencies

Install the required Python packages using `pip`.

```bash
# Install dependencies
pip install -r requirements.txt
```

### 4. Configure API Key

The application requires a Google API key to interact with the Gemini models.

1.  Create a file named `.env` in the root of the project.
2.  Add your API key to the file as follows:

    ```
    GOOGLE_API_KEY="your_api_key_here"
    ```

## Usage

To run the application, execute the main agent script from your terminal.

```bash
# Run the agent workflow
python agents/agents.py
```

The script will then perform the research and summarization for the hardcoded query and print the final result to the console.

## Project Structure

```
.
├── agents/
│   └── agents.py       # Core logic with agent definitions and workflow
├── .env                # (To be created) For storing API keys
├── .env.sh             # Script to activate the virtual environment
├── .gitignore          # Git ignore file
├── GEMINI.md           # Instructional context for the AI agent
├── pyproject.toml      # Project metadata and dependencies
├── README.md           # This file
└── requirements.txt    # Project dependencies for pip
```