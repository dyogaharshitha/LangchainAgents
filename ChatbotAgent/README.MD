
# LangChain Conversational Agent with Movie Database Search

This project demonstrates how to create a conversational AI agent using LangChain and Anthropic’s API (Claude). The agent is designed to answer user queries and interact with a movie database to retrieve relevant information using a custom search function (`tapas_search_question`).

## Features

- **Conversational Agent**: The agent interacts with the user in a conversational style, utilizing memory and tools for dynamic interaction.
- **Movie Database Search**: The agent uses a custom tool (`search_database`) to search a movie database for relevant information.
- **Streaming Responses**: The agent uses the `StreamingStdOutCallbackHandler` to stream responses in real time.
- **Customizable LLM**: The agent uses Anthropic's Claude model for processing queries, but it can easily be switched to a HuggingFace model.

## Prerequisites

- Python 3.x
- Required Python libraries: `langchain`, `langchain_anthropic`, `transformers`, `torch`, `data`
- Anthropic API key for accessing Claude models.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. Install the required dependencies:

   ```bash
   pip install langchain langchain_anthropic transformers torch
   ```

3. Set up your Anthropic API key:
   - Visit [Anthropic API](https://www.anthropic.com/) to get your API key.
   - Replace `"Your-API-key"` in the `llm` initialization section of the code.

4. Install any other required dependencies for the movie database search in `data.py`.

## Setup

### Configuration

- **Agent**: The agent is initialized with the following tools and models:
  - **Movie Database Search Tool** (`tapas_search_question`) that searches a movie database.
  - **Claude Model** from Anthropic for processing queries and generating responses.
  - **HuggingFace Model** (`microsoft/phi-2`) for generating text (optional but configurable).

### Customization

- To switch between the Claude model and a HuggingFace model, uncomment the line where `HuggingFacePipeline` is set up (`llm = HuggingFacePipeline(pipeline=hf_pipeline)`).
- You can modify the `MAX_TURNS` to allow the agent to handle more or fewer interactions before automatically terminating.

### Example Usage

1. Run the Python script:

   ```bash
   python conversational_agent.py
   ```

2. The agent will prompt you for input in the terminal.

   Example interaction:
   ```
   User: Who starred in The Matrix?
   Agent: Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and others.
   ```

3. To terminate the conversation, simply type `terminate`:

   ```
   User: terminate
   Agent: TERMINATE
   ```

### Memory

- The agent uses a **conversation buffer memory** (`ConversationBufferMemory`) to keep track of the dialogue. The memory is updated with each new interaction and used to maintain context.

### Tools

- The `search_database` tool uses the `tapas_search_question` function from `data.py` to query the movie database.
- If you need a different database or tool, modify or replace the tool function in the `tools` list.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **LangChain**: Powerful framework for building language model applications.
- **Anthropic Claude**: Advanced conversational AI model.
- **HuggingFace**: Provides pre-trained models for text generation and processing.
- **Transformers**: HuggingFace's library for working with transformer models.

