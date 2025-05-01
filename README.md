
# 🚀 AI-Powered Conversational Agents and Tools

This repository showcases a series of **AI-driven conversational agents and tools** designed to interact with users, generate insightful comments, and search for relevant information across various domains. The projects leverage cutting-edge frameworks like **LangChain**, **HuggingFace**, and **Anthropic API** to perform tasks such as **generating comments** for LinkedIn posts, **answering questions** based on movie databases, and **enhancing conversational responses**.

The three projects featured here are:

1. **Conversational Agent with Movie Database Search**
2. **Enhanced Conversational Agent**
3. **Multi-Agent LinkedIn Comment Generator (Healthcare Focus)**

---

## 🧠 Projects Overview

### 1. **Conversational Agent with Movie Database Search**
This agent uses **LangChain** and **Anthropic's Claude** model to engage in natural conversations with users, while also querying a movie database for relevant information. It includes a memory buffer to maintain context and streams responses in real time.

**Key Features:**
- Conversational AI that responds with context-aware information.
- Integrated movie database search tool.
- Real-time response streaming with Anthropic's Claude model.

---

### 2. **Enhanced Conversational Agent**
This project enhances conversational interactions using **LangChain** pipelines and custom prompts. The agent first enhances the user input before processing it with an LLM (large language model), which generates a relevant response. It integrates **memory** for context and uses **HuggingFace pipelines** for text generation.

**Key Features:**
- **Prompt Enhancement**: Refines user input to ensure clarity and completeness.
- **Contextual Awareness**: Memory mechanism to remember past interactions.
- **Customizable Pipeline**: Ability to integrate different LLMs or switch between models.

---

### 3. **Multi-Agent LinkedIn Comment Generator (Healthcare Focus)**
This agent system generates **custom comments** on LinkedIn posts, tailored to the healthcare industry. It uses **multiple agents** for different tasks like **researching the post**, **matching it to client interests**, and **generating appropriate comments**. The system ensures high-quality, on-brand engagement while adhering to ethical guidelines.

**Key Features:**
- **Modular Agent Framework**: Multiple agents working collaboratively to analyze, enhance, and respond.
- **Contextual Comment Generation**: Tailored comments based on the healthcare industry and client preferences.
- **Real-Time Web Scraping**: Fetches content from URLs for detailed analysis.

---

## 🚀 How to Run Each Project

### 1. **Conversational Agent with Movie Database Search**

#### Setup
- Clone the repository and install the required dependencies.
  ```bash
  git clone https://github.com/yourusername/yourrepo.git
  cd yourrepo
  pip install -r requirements.txt
  ```
- Ensure you have access to **Anthropic's API key** for the Claude model.
- Run the agent:
  ```bash
  python conversational_agent.py
  ```

---

### 2. **Enhanced Conversational Agent**

#### Setup
- Clone the repository and install the required dependencies.
  ```bash
  git clone https://github.com/yourusername/yourrepo.git
  cd yourrepo
  pip install -r requirements.txt
  ```
- Run the agent:
  ```bash
  python enhanced_conversational_agent.py
  ```

---

### 3. **Multi-Agent LinkedIn Comment Generator (Healthcare Focus)**

#### Setup
- Clone the repository and install the required dependencies.
  ```bash
  git clone https://github.com/yourusername/healthcare-linkedin-commenter.git
  cd healthcare-linkedin-commenter
  pip install -r requirements.txt
  ```
- Add your **Anthropic API key** in the configuration.
- Run the bot:
  ```bash
  python main.py
  ```

---

## 📦 Project Structure

The repository contains the following project files and structure:

```
.
├── conversational_agent.py         # Conversational Agent with Movie Database Search
├── enhanced_conversational_agent.py  # Enhanced Conversational Agent
├── healthcare-linkedin-commenter/   # Multi-Agent LinkedIn Comment Generator (Healthcare Focus)
│   ├── custom_tools.py             # Custom tools like `get_url_content`
│   ├── agent.py                   # Main execution script for LinkedIn commenter
│   └── requirements.txt            # Dependencies for LinkedIn commenter project
├── requirements.txt               # General dependencies for all projects
├── README.md                      # This file
└── LICENSE                        # MIT License
```

---

## ✨ Example Outputs

### 1. **Conversational Agent with Movie Database Search**

Given a query like "Who starred in The Matrix?", the agent might respond:

```
Agent: Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and others.
```

### 2. **Enhanced Conversational Agent**

For a question like "What is the capital of France?", the agent might respond:

```
Agent: The capital of France is Paris.
```

### 3. **Multi-Agent LinkedIn Comment Generator (Healthcare Focus)**

Given a LinkedIn post about **AI in telemedicine**, the system might generate:

```
"Impressive shift toward equitable healthcare! As someone who led a telemedicine rollout, I truly appreciate how AI is bridging care gaps in underserved communities. Exciting times for healthtech."
→ `APPROVE`
```

---

## 🔧 Customization

- **Integrate New Models**: You can swap out the current models with others from HuggingFace or Anthropic.
- **Extend with New Agents**: Add more agents to each project for additional functionality.
- **Modify Search Function**: Customize the movie database search tool or LinkedIn comment generation logic.

---

## 📜 License

MIT License

---

This repository provides a comprehensive showcase of AI-powered conversational agents with various use cases. Whether you're looking to generate dynamic conversations, improve user interaction through enhanced prompts, or generate on-brand comments for LinkedIn, these projects are versatile and ready to be adapted for different needs.

# Design decisions
Here are some **design decisions** that were made in the development of the projects, which are important to understand the architecture and functionality:

---

## Design Decisions

### 1. **Agent Framework Architecture**

#### Decision: Use of Modular Agent System
- **Reasoning**: In the **Multi-Agent LinkedIn Comment Generator** project, multiple agents were used to handle distinct tasks such as analyzing the post, researching healthcare information, matching client profiles, and generating comments. This modular approach allows for easy updates, scalability, and testing of each individual agent.
- **Benefit**: This design allows flexibility in the system. If you want to introduce new agents (e.g., for sentiment analysis, or influencer matching), you can simply add them to the agent framework without overhauling the entire system.

---

### 2. **Use of LangChain for Conversational Memory and Tools**

#### Decision: Use of **LangChain** for managing conversation flow and tools
- **Reasoning**: LangChain is a powerful framework designed for building complex language model-powered applications. For the **Conversational Agent** and **Enhanced Conversational Agent**, it was chosen to handle **conversation history**, **tool usage**, and **memory management**. LangChain’s built-in memory system (`ConversationBufferMemory`) allows the agent to remember context across multiple turns in the conversation, providing a more seamless and coherent experience.
- **Benefit**: This provides a robust system for context handling, especially in longer conversations where maintaining coherence is key. The integration of memory also simplifies the workflow of interacting with external tools and databases, making the conversation more fluid.

---

### 3. **HuggingFace and Anthropic Integration**

#### Decision: Integrating **HuggingFace** and **Anthropic API** for LLM-powered Conversations
- **Reasoning**: We chose to integrate **HuggingFace** models (e.g., `microsoft/phi-2`) for generating conversational responses and **Claude by Anthropic** for its strong conversational capabilities in **real-time response generation**. These models are specifically useful for generating human-like text and can be easily swapped or enhanced in the future.
- **Benefit**: The ability to switch between different models (Claude and HuggingFace) gives the system flexibility. This ensures that the system is adaptable to various contexts or external requirements (such as deployment constraints or cost considerations), while still delivering high-quality results.

---

### 4. **Tool Usage in LangChain Pipelines**

#### Decision: Use of **Tool Chains** for Enhanced Prompt and Response Processing
- **Reasoning**: In the **Enhanced Conversational Agent** and **Conversational Agent with Movie Database Search**, the use of **Tool chains** (via `RunnableMap` and `PromptTemplate`) allows for the separation of tasks and creates a clear pipeline for improving and generating responses. 
  - First, **input enhancement** is done (if needed), then a **query is performed**, and finally, the **response** is generated.
- **Benefit**: This clear modularization allows the logic to be broken down into manageable steps, improving maintainability and enabling debugging and optimization for each step in the chain. It also improves the readability and reusability of the components.

---

### 5. **Streaming and Real-Time Response Handling**

#### Decision: Real-time **Streaming** of Responses
- **Reasoning**: For **real-time interaction**, the **StreamingStdOutCallbackHandler** was used with Anthropic’s Claude API to stream the response gradually as it is generated. This enables users to see the agent’s response almost instantly without waiting for the entire output to finish processing.
- **Benefit**: Provides a more dynamic and user-friendly experience, particularly for interactive use cases like conversational agents or chatbots. This also simulates a natural back-and-forth conversation, which is critical for user engagement.

---

### 6. **Memory and Context Management**

#### Decision: Implement Memory Buffer for Maintaining Context
- **Reasoning**: To keep track of previous interactions, the system uses **memory buffers** (like `ConversationBufferMemory`) for storing the conversation history. This is crucial for the **Enhanced Conversational Agent** and **Movie Database Search** agent to maintain a coherent flow of conversation over multiple turns.
- **Benefit**: This helps maintain context, making the agent’s responses more relevant to the current conversation. The memory management also ensures that each agent can build upon previous responses to generate more informed and contextually accurate replies.

---

### 7. **Modularization of Codebase and Custom Tools**

#### Decision: Codebase Modularization (Custom Tools & Functions)
- **Reasoning**: Custom functions such as `tapas_search_question` for querying a movie database and `get_url_content` for web scraping were modularized to handle specific tasks independently. This keeps the codebase clean and easy to maintain.
- **Benefit**: By keeping tools and functions isolated, you can easily extend the system with new capabilities without interfering with the main pipeline. For example, a new tool can be added to fetch medical research articles or check for compliance without altering the rest of the system.

---

### 8. **API Integration and Security**

#### Decision: Use of **API Keys** and **Environment Variables**
- **Reasoning**: API keys for services like **Anthropic** are sensitive information, and therefore, we decided to load them from **environment variables** rather than hard-coding them into the project files.
- **Benefit**: This improves security by ensuring sensitive data is not exposed in the codebase, especially when the project is shared or deployed to production. It also allows for easy switching of API keys between different environments (development, staging, production).

---

### 9. **Scalability Considerations for Agent Collaboration**

#### Decision: Use of **Asynchronous** and **Modular Agent Collaboration**
- **Reasoning**: To handle more complex or larger-scale interactions, each agent was designed to work asynchronously. This allows them to process tasks in parallel and collaborate without blocking or slowing down the overall system.
- **Benefit**: This approach enhances performance, as each agent can run independently, optimizing time and resources. It also scales better when adding more agents in the future, without significantly impacting system performance.

---

### 10. **User Interaction Flow Design**

#### Decision: **Simple Console-based Interface** for Interaction
- **Reasoning**: For the sake of simplicity and rapid prototyping, the user interaction in all three projects was designed to take place via the console, where the user inputs a question or request, and the agent responds interactively.
- **Benefit**: This keeps the user interface straightforward and minimizes complexity. It also allows recruiters or users to quickly test the system without needing to set up a complex web or graphical interface.

---

These design decisions reflect a focus on **modularity**, **scalability**, and **user-centric experience**. The projects are built with flexibility in mind, allowing for future extensions, updates, and integrations with minimal friction.

