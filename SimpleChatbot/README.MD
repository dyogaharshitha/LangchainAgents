
# LangChain Enhanced Conversational Agent with Movie Database Search

This project demonstrates a conversational AI agent that uses LangChain's enhanced prompt chain to process user inputs, improve prompts for better responses, and access external knowledge (such as a movie database) for generating context-aware answers.

## Features

- **Conversational AI**: The agent processes the conversation context and enhances prompts based on history and current user input.
- **Prompt Enhancement**: The input is rephrased and refined using a specialized prompt template for improved query responses.
- **Movie Database Search**: The agent uses a custom tool (`tapas_search_question`) to search a movie database for relevant information.
- **Memory**: The agent uses `ConversationBufferMemory` to retain context between interactions, ensuring coherent responses across turns.
- **HuggingFace Pipeline**: The agent uses a HuggingFace model (`microsoft/phi-2`) for generating enhanced responses.

## Prerequisites

- Python 3.x
- Required libraries: `langchain_core`, `langchain_community`, `transformers`, `torch`
- Access to a HuggingFace model (`microsoft/phi-2` or your preferred model).
- A movie database search function (`tapas_search_question`) to provide context.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. Install the required dependencies:

   ```bash
   pip install langchain_core langchain_community transformers torch
   ```

3. Install any other required dependencies for the movie database search in `data.py`.

4. Ensure that the model (`microsoft/phi-2`) is available in your HuggingFace model hub, or replace with your own model.

## Setup

### Configuration

- **Enhancer Prompt**: The prompt template for enhancing user input is defined as `enhancer_prompt`. It rephrases the input if necessary.
- **Responder Prompt**: The `responder_prompt` generates a chatbot response based on the enhanced prompt and context.
- **Memory**: `ConversationBufferMemory` is used to store conversation history and ensure context is preserved.

### Customization

- **Change the Model**: You can replace `"microsoft/phi-2"` with any other model of your choice by changing the `model_name` variable and ensuring the model is loaded with the correct tokenizer and pipeline.
  
- **Modify Search Function**: The function `tapas_search_question` is used to query an external database for context. Modify this function to suit your needs (e.g., replace with a different database or API).

### Example Usage

1. Run the Python script:

   ```bash
   python conversational_agent.py
   ```

2. The agent will prompt you for input in the terminal. For example:

   ```
   User: Who is the director of the movie Avatar?
   Agent: James Cameron directed the movie "Avatar."
   ```

3. To terminate the conversation, simply stop the script or break the loop.

### Enhanced Prompt and Response Flow

The flow of how the agent processes a question and responds is as follows:

1. **Enhancer Chain**: Takes user input and context from conversation memory, enhances the prompt if necessary.
2. **Knowledge Base Query**: Uses the `tapas_search_question` function to search for relevant data based on the enhanced prompt.
3. **Responder Chain**: Takes the enhanced prompt and knowledge, then generates the response using a conversational AI model.
4. **Memory**: Saves the conversation context for future interactions, ensuring coherent responses.

## Example Code Snippet

```python
# Example of running the pipeline
if __name__ == "__main__":
    for i in range(3):
        question = input("User: ")
        context = tapas_search_question(question)  # Search for context
        print(run_pipeline(question, context))  # Run the enhanced pipeline
```

In this example, the agent processes a question from the user, enhances the prompt, retrieves knowledge, and responds accordingly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **LangChain**: Framework for building powerful language model applications.
- **HuggingFace**: The `transformers` library for pre-trained language models.
- **ConversationBufferMemory**: Essential for maintaining a memory of the ongoing conversation.
- **tapas_search_question**: Custom function to query external data (e.g., a movie database).

